from fabric.api import task, execute, runs_once, parallel, hosts, env
from fabric.api import local, lcd
import os.path
import os
import json
from multiprocessing import cpu_count
#from fabric.api import cd, run
#from fabric.contrib.files import upload_template

from jinja2 import Environment, FileSystemLoader

env.user = "root"
WORKERS = cpu_count() + 1
IPXE_WORK_DIR = "work/ipxe"
WEB_WORK_DIR = "work/www"
IPXE_EMBEDDED = "work/media.ipxe"
IPXE_EMBED_TEMPLATE = "bootmedia.ipxe"
IPXE_BOOTSTRAP = "bootstrap.ipxe"
BOOTSTRAP_HOST = "cdn.ubooty.org"
TEMPLATE_DIR = os.path.join(os.getcwd(), 'templates')

jinjaEnv = Environment(loader=FileSystemLoader(TEMPLATE_DIR))


@runs_once
@hosts('localhost')
@task
def ipxe_clone(repo="git://git.ipxe.org/ipxe.git"):
    local("git clone --depth=10 %s %s" % (repo, IPXE_WORK_DIR))


@runs_once
@hosts('localhost')
@task
def ipxe_build():
    with lcd("%s/src" % IPXE_WORK_DIR):
        local("make clean")
        local("make -s -j%d EMBED=%s" % (
            WORKERS, os.path.abspath(IPXE_EMBEDDED)))


@runs_once
@hosts('localhost')
@task
def ipxe_embedded(source=BOOTSTRAP_HOST):
    with open(IPXE_EMBEDDED, 'w+') as w:
        t = jinjaEnv.get_template(IPXE_EMBED_TEMPLATE)
        w.write(t.render(host=source))


@task
def media():
    if not os.path.exists(IPXE_WORK_DIR):
        execute(ipxe_clone)
    execute(ipxe_embedded)
    execute(ipxe_build)


@task
def bootstrap():
    menu = {}
    variables = {}
    for root, dirs, files in os.walk(TEMPLATE_DIR):
        name = None
        try:
            if 'menu.json' in files:
                name = os.path.basename(root)
                t = jinjaEnv.get_template(os.path.join(name, 'menu.json'))
                menu[name] = json.loads(t.render())
            else:
                continue

            if 'var.json' in files:
                t = jinjaEnv.get_template(os.path.join(name, 'var.json'))
                variables.update(json.loads(t.render()))

            # TODO upload remaing files
        except ValueError:
            print "Error processing", name

    # TODO process bootstrap.ipxe template
    # print menu
    print variables


@task
@parallel
def build():
    # build binaries locally
    execute(media)
    # jinja up bootstrap.ipxe
    execute(bootstrap)
    # jinja up nginx configs
    execute(webserver)

# Ubooty - The universal bootstrapper

Ubooty is the universal bootstrapper for Linux.  It combines the best of open source tools to make installing Linux easy.  No more downloading large DVDs or working through complicated DHCP/PXE setups.  

## Requirements

* DHCP server
* Working internet without forced proxies (sorry!)
* Formattable USB or blank (CD)VD

## Download

[USB](http://cdn.ubooty.org/ubooty-latest.usb) [ISO](http://cdn.ubooty.org/ubooty-latest.iso) 

## Advanced downloads

Most users won't need these, but they are good for GRUB/Syslinux and existing DHCP environments.

[Linux kernel](http://cdn.ubooty.org/ubooty-latest.lkrn) [PXE](http://cdn.ubooty.org/ubooty-latest.undionly)

### USB

Linux: ```sudo dd if=ubooty.usb of=/dev/sdX```  
Windows: Use [Winimager](http://sourceforge.net/projects/win32diskimager/)

### ISO

Linux: Use k3b or cdrecord  
Windows: Use [CD Burner XP](http://cdburnerxp.se/en/home) or something that can burn ISO Files

### Linux kernel (advanced)

You can use this linux kernel formatted image to boot it via GRUB or add it to your current Syslinux bootmedia.

### PXE (advanced)

This is a UNDI driver (no hardware drivers).  You should probably check out the iPXE [chainloading documentation](http://ipxe.org/howto/chainloading).

# Contributing

Fork, follow the guidelines, commit, submit pull request.  Pretty simple.

## Guidelines

* **MUST** have minimal installation type
* **CAN** have a *full/rich* installation type
* **SHOULD NOT** automate any partitioning or formatting of disks (unless it's an appliance)
* **MUST** have descriptive, but brief menu text
* **SHOULD NOT** have 32 and 64-bit versions of the installer.  64bit or go home. Unless it's ARM or something special.

## Appliance guideline exceptions

Appliances such as [OpenELEC](http://openelec.tv) are designed to be installed and operated a certain way.  Because of this, some additional guidelines for appliances need to exist that supercede the base Guidelines.

* **CAN** have a minimal install type
* **SHOULD** have a *full/rich* install type
* **CAN** automate partitioning and formatting of disks (though still discouraged, or at least semi automated)


# Credits

Sofware used in the making of this project.  Thanks to them for making awesome software!

* [iPXE](http://ipxe.org)
* [Syslinux](http://syslinux.zytor.com)
* [Fabric](http://fabfile.org/)


#!/bin/sh
path=`pwd`

echo $path
# set folder for machine
VBoxManage setproperty machinefolder ${path}/machine


# create and register machine
VBoxManage createvm --name "OSnova" --ostype "Debian12_64" --default --register 

#create virtual hard drive
# VBoxManage createhd --filename "/media/data/autoinstall_tests/machine/osnova_test1.vdi" --size 25000 --format VDI 
VBoxManage createhd --filename "machine/osnova_test.vdi" --size 25000 --format VDI 

# adding SATA controller to machine
#VBoxManage storagectl "OSnova" --name "SATA Controller" --add sata --controller IntelAhci

# attaching hard drive to machine
VBoxManage storageattach "OSnova" --storagectl "SATA" --port 0 --device 0 --type hdd --medium "machine/osnova_test.vdi"

# adding IDE controller
VBoxManage storageattach "OSnova" --storagectl "IDE" --port 1 --device 0 --type dvddrive --medium "iso/onyx3-testing-disk1.iso"

# setting hardware parameters
VBoxManage modifyvm "OSnova" --memory 4096 --vram 128 --cpus 4 #--nic1 Bridged


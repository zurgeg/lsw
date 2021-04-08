#!/bin/bash
qemu-sytem-x86-64 \
	-machine q35,kernel_irq_chip=on,accel=kvm \
	-device ich9-ahci,id=sata \
	-drive id=Windows_10_Installer,if=none,format=raw,file="Windows_10_Installer.iso" \
	-device ide-hd,bus=sata.0,drive=Windows_10_Installer \
	-vga qxl \
	
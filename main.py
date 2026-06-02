#!/usr/bin/python3

import os
import time
import platform
import cpuinfo 
import sys
import random
import psutil
import shutil

ascii = r'''
  ___         _               ___       __                    _   _          
 / __|_  _ __| |_ ___ _ __   |_ _|_ _  / _|___ _ _ _ __  __ _| |_(_)___ _ _  
 \__ \ || (_-<  _/ -_) '  \   | || ' \|  _/ _ \ '_| '  \/ _` |  _| / _ \ ' \ 
 |___/\_, /__/\__\___|_|_|_| |___|_||_|_| \___/_| |_|_|_\__,_|\__|_\___/_||_|
      |__/                                                                   
'''

cpu = cpuinfo.get_cpu_info()["brand_raw"]

if platform.system() == "Windows":
    os.system("cls")
else :
    os.system("clear")
print(ascii)
ramamount = psutil.virtual_memory().total / (1024 ** 3)
print("You are running on " + platform.system() + "!")
print(f"Your CPU is the {cpu} and has {os.cpu_count()} cores!")
print(f"You have {ramamount:.0f} GB of RAM and have {psutil.virtual_memory().available / (1024 ** 3):.0f} GB free")
print(f"You are running this from {os.getcwd()}")
print(f"There is {len(psutil.disk_partitions())} storage drives connected to your computer!")
print(f"The drive you are running this script of has {shutil.disk_usage(os.getcwd()).free / (1024 ** 3):.0f}GB of storage left out of {shutil.disk_usage(os.getcwd()).total / (1024 ** 3):.0f}GB")
if platform.system() == ("Linux"):
    if os.path.exists("/etc/debian_version"):
        print("You are running on the distro Debian!")
    if os.path.exists("/etc/arch-release"):
        print("You are running on an Arch-based Distro!")
print(" ")
print(" ")

pkgyes = input("Would you like to install any packages on your computer? ")
if "yes" in pkgyes:
    pkgname = input("What package do you want to install? ")
    if platform.system() == ("Windows"):
        print("Running on Windows, using winget....")
        os.system(f"winget install {pkgname}")
    if platform.system == "Darwin":
        print("Sorry, Darwin/macOS is unsupported for the time being (Updates and Installing Packages)")
    if platform.system() == ("Linux"):
        if os.path.exists("/etc/apt/apt.conf.d"):
            print("APT detected, using that instead....")
            os.system(f"apt install {pkgname}")
        if os.path.exists("/etc/pacman.conf"):
            print("Pacman detected, using that instead....")
            os.system(f"pacman -Sy {pkgname}")
        if os.path.exists("/etc/dnf/dnf.conf"):
            print("DNF detected, using DNF....")
            os.system(f"dnf install {pkgname}")
        if os.path.exists("/etc/bashrc_Apple_Terminal"):
            print("Sorry, macOS isn't supported yet...")
        if os.path.exists("/data/data/com.termux/files/usr"):
            print("Detected pkg, instaling with pkg....")
            os.system(f"pkg install {pkgname} -y")
        if os.path.exists("/etc/pkg"):
            print("Detected pkg, instaling with pkg....")
            os.system(f"pkg install {pkgname} -y")
        if os.path.exists("/etc/zypp/zypper.conf"):
            print("Running with zypper....")
            os.system(f"sudo zypper install {pkgname}")
updyes = input("Would you like to update your computer? ")
if "yes" in updyes:
    if platform.system() == "Linux":
        if os.path.exists("/etc/apt/apt.conf.d"):
            print("Running on APT. ")
            os.system("sudo apt update && apt upgrade -y ")
        if os.path.exists("/etc/pacman.conf"):
            print("Pacman detected.")
            os.system("sudo pacman -Syu")
        if os.path.exists("/etc/dnf/dnf.conf"):
            print("Using DNF.")
            os.system("sudo dnf upgrade --refresh")
        if os.path.exists("/data/data/com.termux/files/usr"):
            print("Using pkg/apt.")
            os.system("pkg update && pkg upgrade -y")
        if os.path.exists("/etc/pkg"):
            print("Using pkg to update...")
            os.system("pkg update && pkg upgrade -y")
        if os.path.exists("/etc/zypp/zypper.conf"):
            os.system("sudo zypper dup -y")
    if platform.system() == "Darwin":
        print("Sorry, Darwin/macOS is unsupported for the time being (Updates and Installing Packages)")
    if platform.system() == "Windows":
        print("Sorry, Windows is unsupported to update for the time being, but you can install packages though!")  

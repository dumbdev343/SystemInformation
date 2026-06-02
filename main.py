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
print(f"You have {ramamount:.0f} GB of RAM")
print(f"You are running this from {os.getcwd()}")
print(f"There is {len(psutil.disk_partitions())} storage drives connected to your computer!")
print(f"The drive you are running this script of has {shutil.disk_usage(os.getcwd()).free / (1024 ** 3):.0f}GB of storage left out of {shutil.disk_usage(os.getcwd()).total / (1024 ** 3):.0f}GB")
if platform.system() == ("Linux"):
    if os.path.exists("/etc/debian_version"):
        print("You are running on the distro Debian!")
print(" ")
print(" ")

pkgyes = input("Would you like to install any packages on your computer? ")
if "yes" in pkgyes:
    pkgname = input("What package do you want to install?")
    if platform.system == "Windows":
        print("Running on Windows, using winget....")
        os.system(f"winget install {pkgname}")
    if platform.system == ("Linux"):
        if os.path.exists("/etc/debian_version"):
            print("Running on Debian, using apt....")
            os.system(f"apt install {pkgname}")
        if os.path.exists("/etc/arch-release")
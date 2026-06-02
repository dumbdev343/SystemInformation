# System Information 💻


This is a tool designed for people who need to view system info quickly alongside installing programs

# Well what can it do?
- Print CPU Information
- Print RAM Information
- Print Storage Information
- Print GPU Information (soon)
- Print the platform you are running on
- Where you are running the script for stuff like Active Directory where you have profiles on NASes and need to verify that it's actually on the NAS not locally.
- Install packages on your computer, including various Linux distros from Arch all the way through to OpenSUSE Tumbleweed
- Update your computer for you automaticly (Linux only as of right now soon)


# How can I run it?
First you need to download the script for Linux (maybe macOS aswell?) unless you prefer manually (your choice)

One Liner
```sh
curl -LO https://raw.githubusercontent.com/dumbdev343/SystemInformation/refs/heads/main/LinuxInstaller.sh && bash LinuxInstaller.sh
```

Manually
```sh
git clone https://github.com/dumbdev343/systeminformation.git
cd systeminformation
pip install -r requirements.txt
python main.py ## or sudo install -Dm755 /yourpath/main.py /usr/bin/systeminfo

```

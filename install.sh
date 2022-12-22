#!/bin/bash
# installer for Scrapes
# created by : Tobias Karuth (TKAMING)
# staging
echo [*] Staging process...
mkdir ~/.Scrapes
cd ..
mv Scrapes/* ~/.Scrapes
rm -rf Scrapes
cd ~/.Scrapes
echo [+] Completed

#  get tools
echo [*] Installing tools...
sudo apt update
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install -e .
sudo pip3 install selenium
sudo wget https://github.com/mozilla/geckodriver/releases/download/v0.32.0/geckodriver-v0.32.0-linux64.tar.gz
sudo tar -xvf geckodriver-v0.32.0-linux64.tar.gz
sudo rm geckodriver-v0.32.0-linux64.tar.gz
sudo chmod +x geckodriver
echo [+] Completed

# clean up
echo [+] Installation Completed
echo "1. restart your Computer"
echo "2. you can type 'scrapes [ARGUMENT]' to launch Scrapes"

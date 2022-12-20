#!/bin/bash
# installer for Scrapes
# by Tobias Karuth (TKAMING)


echo [*] Staging process...
mkdir ~/.Scrapes
cd ..
mv Scrapes/* ~/.Scrapes
rm -rf Scrapes
cd ~/.Scrapes
echo [+] Completed

echo [*] Installing tools...
sudo apt update
sudo apt-get install python3
echo [+] Completed

echo [*] Setting up alias...
echo "alias scrapes=\"python3 $(pwd)/main.py\"" >> ~/.bashrc
echo "alias scrapes=\"python3 $(pwd)/main.py\"" >> ~/.zshrc
echo [+] Completed

echo [+] Installation Completed
echo "- please restart your terminal"
echo "- type 'scrapes' to launch Scrapes"

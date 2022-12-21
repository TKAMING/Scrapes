#!/bin/bash
# installer for Scrapes
# created by : Tobias Karuth (TKAMING)

#  get tools
echo [*] Installing tools...
sudo apt update
sudo apt-get install python3
sudo apt-get install pip3
echo [+] Completed

#installing
pip3 install -e .

# clean up
echo [+] Installation Completed
echo "- please restart your terminal"
echo "- please type 'scrapes [ARGUMENT]' to launch Scrapes"

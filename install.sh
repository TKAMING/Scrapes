#!/bin/bash
# installer for Scrapes
# created by : Tobias Karuth (TKAMING)
# staging
echo [*] Staging process...
mkdir ~/.Scrapes
cd ..
sudo mv Scrapes/* ~/.Scrapes
sudo rm -rf Scrapes
cd ~/.Scrapes
echo [+] Completed

#  get tools
echo [*] Installing tools...
sudo apt update
sudo apt-get install python3
sudo apt-get install python3-pip
sudo pip3 install -e .
sudo pip3 install Scweet==1.8
sudo pip3 install certifi
sudo pip3 install selenium==4.2.0
sudo pip3 install pandas
sudo pip3 install python-dotenv
sudo pip3 install chromedriver-autoinstaller
sudo pip3 install geckodriver-autoinstaller
sudo pip3 install urllib3
cd ..
echo [+] Completed

# clean up
echo [+] Installation Completed
echo "1. restart your Computer"
echo "2. you can type 'scrapes [ARGUMENT]' to launch Scrapes"
echo "REQUIREMENTS: You need to install Chrome to use the Twitter scrape function!!!"

#!/bin/bash
# installer for the Chrome driver for the selenium use (Linux)
# created by : Tobias Karuth (TKAMING)

echo [*] Installing chromedriver
cd ~/.Scrapes
sudo wget https://chromedriver.storage.googleapis.com/94.0.4606.41/chromedriver_linux64.zip
sudo unzip chromedriver_linux64.zip
sudo chmod +x chromedriver
sudo rm -rf chromedriver_linux64.zip
cd ..
echo [+] Installation Completed
chromedriver --version

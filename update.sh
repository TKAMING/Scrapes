#!/bin/bash

# remove previous version
cd ~
sudo rm -rf .Scrapes

# install new version
sudo git clone https://github.com/TKAMING/Scrapes

# install dependencies
cd Scrapes
sudo chmod +x install.sh
bash install.sh

# self delete
sudo rm -rf ../update.sh
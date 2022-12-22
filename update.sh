#!/bin/bash

# remove previous version
cd ~
rm -rf .Scrapes

# install new version
git clone https://github.com/TKAMING/Scrapes

# install dependencies
cd Scrapes
chmod +x install.sh
./install.sh

# self delete
rm -rf ../update.sh
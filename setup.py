from setuptools import setup
import os

#version = os.system("sudo curl https://raw.githubusercontent.com/TKAMING/Scrapes/main/version.txt")

setup(
    name = 'Scrapes',
    version = 1.8,
    packages = ['scrapes'],
    license = "MIT License",
    install_requires=['Chrome'],
    entry_points = {
        'console_scripts': [
            'scrapes = scrapes.__main__:main'
        ]
    })
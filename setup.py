from setuptools import setup
import os

version = os.system(f"sudo curl https://raw.githubusercontent.com/TKAMING/Scrapes/main/version.txt")

setup(
    name = 'Scrapes',
    version = version,
    packages = ['scrapes'],
    license = "MIT License",
    install_requires=['chromedriver', 'Chrome'],
    entry_points = {
        'console_scripts': [
            'scrapes = scrapes.__main__:main'
        ]
    })
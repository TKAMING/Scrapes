from setuptools import setup

setup(
    name = 'Scrapes',
    version = 1.9,
    packages = ['scrapes'],
    license = "MIT License",
    #install_requires=['Chrome'],
    entry_points = {
        'console_scripts': [
            'scrapes = scrapes.__main__:main'
        ]
    })
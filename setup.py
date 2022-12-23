from setuptools import setup
setup(
    name = 'Scrapes',
    version = '0.4.1',
    packages = ['scrapes'],
    license = "MIT License",
    entry_points = {
        'console_scripts': [
            'scrapes = scrapes.__main__:main'
        ]
    })
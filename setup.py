from setuptools import setup
setup(
    name = 'Scrapes',
    version = '1.3',
    packages = ['scrapes'],
    license = "MIT License",
    entry_points = {
        'console_scripts': [
            'scrapes = scrapes.__main__:main'
        ]
    })
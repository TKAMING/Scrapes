from setuptools import setup
setup(
    name = 'Scrapes',
    version = '0.1.0',
    packages = ['scrapes'],
    entry_points = {
        'console_scripts': [
            'scrapes = scrapes.__main__:main'
        ]
    })
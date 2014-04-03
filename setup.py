#!/usr/bin/python

import setuptools

setuptools.setup(
    install_requires=open('requires.txt').readlines(),
    version = 3,
    name = 'askbot',
    packages = ['askbot'],
    entry_points = {
        'console_scripts': [
            'askbot = askbot.shell:main',
        ],
    }
)


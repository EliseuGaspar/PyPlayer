#!/usr/bin/python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name = "Py_Player",
    version = '1.0.0',
    author = 'Eliseu Gaspar',
    author_email = 'eliseugaspar4@gmail.com',
    packages = ['Py_Player'],
    description = 'Um Pacote perfeito para audios mp3',
    long_description = 'PyPlayer é um modúlo para manipulação de áudios no formato MP3.\
    O mesmo foi criado com o objectivo de ser um modúlo fácil de usar e completo no \
    contexto de manipulação de MP3.',
    url = 'https://github.com/EliseuGaspar/PyPlayer',
    project_urls = {
        'Código fonte': 'https://github.com/EliseuGaspar/PyPlayer',
        'Download': 'https://github.com/EliseuGaspar/PyPlayer/archive/refs/heads/master.zip'
    },
    license = 'MIT',
    keywords = [
        "player","mp3",
        'audio','pacote para audio'
    ],
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Angola)',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        "Pygame",
        "Mutagen"
    ]
)
#!/bin/bash
# Ativa o ambiente virtual e roda o extract.py
pkill chrome
pkill chromedriver
# Caminho até a pasta do projeto
cd /home/figas/Desktop/FocoRadical
# Ativa o venv
source venv/bin/activate
pip install selenium webdriver-manager
# Executa o script Python
/usr/bin/python3 /home/figas/Desktop/FocoRadical/extract.py

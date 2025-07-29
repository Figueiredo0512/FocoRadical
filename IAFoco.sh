#!/bin/bash
export PATH=/usr/local/bin:/usr/bin:/bin
export HOME=/home/vboxuser
export DISPLAY=:0

# Mate possíveis instâncias abertas
pkill -f chrome
pkill -f chromedriver

# Vá para a pasta do projeto
cd /home/vboxuser/Desktop/FocoRadical

# Ativa o virtualenv
source venv/bin/activate

# NÃO usar pip install aqui — já instalamos antes
# Apenas roda o script
python3 extract.py


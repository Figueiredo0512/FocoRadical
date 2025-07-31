#!/bin/bash
export PATH=/usr/local/bin:/usr/bin:/bin
export HOME=/home/vboxuser
export DISPLAY=:0

# Limpa eventuais perfis antigos
rm -rf /tmp/selenium_profile

# Mate possíveis instâncias abertas
pkill -f chrome
pkill -f chromedriver

# Vá para a pasta do projeto
cd /home/vboxuser/Desktop/FocoRadical

# Ativa o virtualenv
source venv/bin/activate
python3 extract.py
upload_github.sh

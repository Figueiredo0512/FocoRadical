#!/bin/bash
# Caminho do repositório

cd /home/vboxuser/Desktop/FocoRadical || exit

# Atualiza repositório local
git pull origin main

# Adiciona todos os arquivos novos ou alterados
git add .

# Commit com data e hora
git commit -m "Atualização automática: $(date '+%Y-%m-%d %H:%M:%S')"

# Envia pro GitHub
git push origin main

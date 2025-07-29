#!/bin/bash
# Caminho do repositório
cd /home/vboxuser/Desktop/FocoRadical
git status

git add .

git commit -m "Atualização automática: $(date '+%Y-%m-%d %H:%M:%S')"

git push origin main

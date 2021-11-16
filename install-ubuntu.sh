#!/usr/bin/env bash

sudo apt install -y python3 python3-pip libopengl0
pip3 install -r requirements.txt

echo "****************************************"
echo "L'installation est terminée, vous pouvez lancer Consmaster avec les commandes:"
echo "cd src"
echo "python3 consmaster.py"

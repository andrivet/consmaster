#!/usr/bin/env bash

sudo apt install -y python3 python3-pip libopengl0
pip3 install -r requirements.txt

echo "****************************************"
echo "L'installation est terminée, vous pouvez lancer Consmaster avec la commande:"
echo "python3 src/consmaster.py"

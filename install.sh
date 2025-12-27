#!/bin/bash
echo "Instalando Code2pkg SDK - Sony Key Breakers..."
if [ -d "/data/data/com.termux/files/usr/bin" ]; then
    pkg update && pkg install -y python clang make binutils
else
    sudo apt-get update && sudo apt-get install -y python3 python3-pip clang make
fi
pip install pycryptodome colorama
chmod +x c2p
chmod +x core/*.py
echo "Instalação concluída! Digite ./c2p para começar."
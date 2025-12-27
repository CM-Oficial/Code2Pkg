#!/bin/bash
echo "Instalando Code2pkg SDK - Sony Key Breakers..."

# Cria a pasta de projetos que o C2P vai consultar
mkdir -p projects

if [ -d "/data/data/com.termux/files/usr/bin" ]; then
    pkg update && pkg install -y python clang make binutils
else
    sudo apt-get update && sudo apt-get install -y python3 python3-pip clang make
fi

pip install pycryptodome colorama
chmod +x c2p

# Ajustado para garantir que a pasta core existe antes do chmod
if [ -d "core" ]; then
    chmod +x core/*.py
fi

echo "Instalação concluída! Digite ./c2p para começar."

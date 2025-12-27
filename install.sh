#!/bin/bash
echo "Instalando Code2pkg SDK - Sony Key Breakers..."

# Cria a pasta de projetos e um arquivo oculto para o Git não ignorá-la
mkdir -p projects
touch projects/.gitkeep

if [ -d "/data/data/com.termux/files/usr/bin" ]; then
    pkg update && pkg install -y python clang make binutils
else
    sudo apt-get update && sudo apt-get install -y python3 python3-pip clang make
fi

# Instalação das dependências de Python
pip install pycryptodome colorama

# Permissões nos scripts que estão no root
chmod +x c2p
chmod +x *.py

echo "Instalação concluída! Digite ./c2p para começar."

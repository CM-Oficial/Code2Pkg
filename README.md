# 🎮 Code2pkg (C2P) - PS3 SDK

![Status](https://img.shields.io/badge/Status-Stable-green)
![Exploit](https://img.shields.io/badge/Keys-Via_Exploit-red)
![Group](https://img.shields.io/badge/Made_by-Sony_Key_Breakers-blue)

**Code2pkg (C2P)** é um SDK completo e portátil para desenvolvimento de homebrew no PlayStation®3. Diferente de outras toolchains, o C2P já integra o motor de assinatura **SKB Engine**, permitindo a criação de pacotes (.pkg) válidos sem a necessidade de ferramentas externas.

---

## 🔑 Créditos de Descoberta
As chaves de criptografia e o método de assinatura integrados nesta ferramenta foram obtidos via exploit por:
**👤 muriloopr_ (Sony Key Breakers)**

---

## 🛠️ Funcionalidades
* **Wizard Interativo**: Configuração rápida de Title ID e metadados.
* **MDPS3C Engine**: Compilação via Clang otimizada para o processador Cell (PowerPC).
* **Assinatura Real**: Injeção de RIV e Priv Key para EBOOTs e PKGs funcionais.
* **Termux Ready**: Desenvolva e assine seus jogos diretamente do Android.

## 🚀 Instalação

1. Clone o repositório ou baixe o ZIP.
2. No terminal (Linux ou Termux), execute:
```bash
chmod +x install.sh
./install.sh

Como Usar
Criar Projeto: ./c2p init "NomeDoApp"

Compilar: Entre na pasta do projeto e use: ../c2p build

Gerar PKG: ../c2p pkg

⚠️ WARNING!
This project was created to assist in the creation of PKG files for the PlayStation®3 system. We DO NOT SUPPORT any form of piracy of PS3® software. This is a tool for developers and homebrew enthusiasts.

Enjoy! <3
 
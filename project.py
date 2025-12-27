import os
from core.sfo_gen import SFOGenerator

def create_project_structure(name):
    print(f"[*] Criando projeto {name}...")
    os.makedirs(f"{name}/src", exist_ok=True)
    os.makedirs(f"{name}/pkg_root/USRDIR", exist_ok=True)
    
    tid = input("Title ID (9 char): ").upper() or "SKB000001"
    
    sfo = SFOGenerator()
    sfo.add_entry("TITLE", name)
    sfo.add_entry("TITLE_ID", tid)
    
    with open(f"{name}/pkg_root/PARAM.SFO", "wb") as f: f.write(sfo.build())
    with open(f"{name}/src/main.c", "w") as f:
        f.write("#include <stdio.h>\nint main() { printf(\"SKB SDK Running!\\n\"); return 0; }")
    # Copia o Makefile do template para a pasta do projeto
    os.system(f"cp templates/Makefile {name}/")
    print("[✔] Projeto inicializado.")
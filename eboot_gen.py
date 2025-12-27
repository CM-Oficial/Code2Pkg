import sys
import struct
import binascii
import os

def make_eboot(elf_in, folder_out):
    # Chaves SKB via exploit
    RIV = binascii.unhexlify("F9205F46F6021697E670F13DFA726212")
    PRIV = binascii.unhexlify("001AD976FCDE86F5B8FF3E63EF3A7F94E861975BA3")

    # --- CORREÇÃO DE CAMINHO ---
    # folder_out é 'projects/teste', então eboot_path vira 'projects/teste/EBOOT.BIN'
    eboot_path = os.path.join(folder_out, "EBOOT.BIN")

    with open(elf_in, "rb") as f:
        elf_data = f.read()

    print(f"[*] SKB Engine: Selando EBOOT com chaves de exploit...")

    # Cabeçalho SCE + RIV + Dados
    header = struct.pack(">4sII", b'SCE\0', 2, 1) # Magic, Version, Type
    
    try:
        with open(eboot_path, "wb") as f:
            f.write(header)
            f.write(RIV) # Injeção direta da RIV
            f.write(elf_data) # O código compilado pela MDPS3C
        print(f"[✔] EBOOT.BIN selado em: {eboot_path}")
    except Exception as e:
        print(f"[!] Erro ao gravar EBOOT: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        # sys.argv[1] é o output.elf, sys.argv[2] é a pasta do projeto
        make_eboot(sys.argv[1], sys.argv[2])
    else:
        print("Uso: python eboot_gen.py <elf_in> <pasta_destino>")

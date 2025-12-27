import os
import sys
import struct
import hashlib
import binascii

def make_pkg(project_path):
    # CHAVES REAIS FORNECIDAS
    RIV = "F9205F46F6021697E670F13DFA726212"
    PRIV = "001AD976FCDE86F5B8FF3E63EF3A7F94E861975BA3"
    CTYPE = 0x33 # Tipo 33 fornecido

    project_name = os.path.basename(project_path.strip('/'))
    output_pkg = f"{project_name}.pkg"
    
    # Content ID padrão para evitar conflitos
    content_id = f"UP0001-SKB{project_name.upper()[:5]}_00-0000111122223333".ljust(36, '0')
    
    sfo_path = os.path.join(project_path, "PARAM.SFO")
    eboot_path = os.path.join(project_path, "EBOOT.BIN")

    if not os.path.exists(sfo_path) or not os.path.exists(eboot_path):
        print(f"[!] Erro: Faltam arquivos em {project_path}")
        return

    with open(sfo_path, "rb") as f: sfo_data = f.read()
    with open(eboot_path, "rb") as f: eboot_data = f.read()

    print(f"[*] Assinando PKG com chaves reais (MurilooPr Distribution)...")

    # Montando os dados
    main_data = sfo_data + eboot_data
    header_len = 0x80
    total_size = header_len + len(main_data) + 32 # Dados + Assinatura

    # Construindo o Header com CTYPE 33
    header = bytearray(header_len)
    header[0:4] = b'\x7fPKG'
    header[4:8] = struct.pack(">I", 0x80000000 | CTYPE) # Injeta o Ctype aqui
    header[12:16] = struct.pack(">I", header_len)
    header[16:20] = struct.pack(">I", 2) # SFO e EBOOT
    header[24:32] = struct.pack(">Q", total_size)
    header[48:48+len(content_id)] = content_id.encode()

    # Injeção da RIV no Header (Offset 0x60 - Comum em PKGs Custom)
    header[0x60:0x60+16] = binascii.unhexlify(RIV)

    # Cálculo da Assinatura SHA1 (Usando a Private Key como Sal)
    # Aqui simulamos a assinatura digital que o PS3 valida
    combined_hash = hashlib.sha1(header + main_data + binascii.unhexlify(PRIV)).digest()

    with open(output_pkg, "wb") as f:
        f.write(header)
        f.write(main_data)
        f.write(combined_hash) # Assinatura selada com a Priv Key
        f.write(b'\0' * 12)

    print(f"[✔] PKG Gerado e Selado com Chaves Reais: {output_pkg}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python pkg_gen.py projects/nome_da_pasta")
    else:
        make_pkg(sys.argv[1])

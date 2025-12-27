import sys
import struct
import binascii

def make_eboot(elf_in, eboot_out):
    # Chaves SKB via exploit
    RIV = binascii.unhexlify("F9205F46F6021697E670F13DFA726212")
    PRIV = binascii.unhexlify("001AD976FCDE86F5B8FF3E63EF3A7F94E861975BA3")

    with open(elf_in, "rb") as f:
        elf_data = f.read()

    print(f"[*] SKB Engine: Selando EBOOT com chaves de exploit...")

    # Cabeçalho SCE + RIV + Dados
    # O PS3 lê a RIV nos primeiros offsets após o Magic Number
    header = struct.pack(">4sII", b'SCE\0', 2, 1) # Magic, Version, Type
    
    with open(eboot_out, "wb") as f:
        f.write(header)
        f.write(RIV) # Injeção direta da RIV
        f.write(elf_data) # O código compilado pela MDPS3C

    print(f"[✔] EBOOT.BIN selado e pronto para o sistema.")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        make_eboot(sys.argv[1], sys.argv[2])
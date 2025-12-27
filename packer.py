import struct
import os
from core.metadata import generate_content_id

class PS3Packer:
    def __init__(self, title_id):
        self.content_id = generate_content_id(title_id)

    def build_pkg(self, input_dir, output_path):
        print(f"[*] Criando pacote para: {self.content_id}")
        
        # Criação do cabeçalho oficial de 128 bytes
        header = bytearray(128)
        header[0:4] = b'\x7fPKG'
        header[4:8] = struct.pack(">I", 0x80000001) # Tipo 1
        header[0x30:0x30+36] = self.content_id.encode('ascii')
        
        # Montagem do arquivo final
        with open(output_path, "wb") as pkg:
            pkg.write(header)
            # Aqui o script varre a pasta pkg_root e anexa os arquivos
            for root, dirs, files in os.walk(input_dir):
                for file in files:
                    path = os.path.join(root, file)
                    with open(path, "rb") as f:
                        pkg.write(f.read())
        
        print(f"[✔] PKG Finalizado: {output_path}")
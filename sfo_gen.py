import struct
import sys
import os

class SFOGenerator:
    def __init__(self): 
        self.entries = []
    
    def add_entry(self, key, val): 
        self.entries.append({'k': key, 'v': val})
    
    def build(self):
        self.entries.sort(key=lambda x: x['k'])
        count = len(self.entries)
        keys, vals, index = b"", b"", b""
        k_off, v_off = 0, 0
        for e in self.entries:
            k_b = e['k'].encode() + b'\x00'
            v_b = e['v'].encode() + b'\x00'
            v_len = len(v_b)
            v_max = (v_len + 3) & ~3
            # Formato do index: key_offset, data_type, data_len, data_max_len, data_offset
            index += struct.pack("<HHIII", k_off, 0x0404, v_len, v_max, v_off)
            keys += k_b
            vals += v_b.ljust(v_max, b'\x00')
            k_off += len(k_b)
            v_off += v_max
        
        # Header: magic, version, key_table_start, data_table_start, entries_count
        h = struct.pack("<4sIIII", b'\x00PSF', 0x101, 20+count*16, 20+count*16+len(keys), count)
        return h + index + keys + vals

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python sfo_gen.py <nome_app> <title_id> <pasta_destino>")
        sys.exit(1)

    nome_app = sys.argv[1]
    title_id = sys.argv[2]
    pasta_destino = sys.argv[3]

    # --- A CORREÇÃO ESTÁ AQUI ---
    # Unimos a pasta 'projects/teste' com o nome do arquivo 'PARAM.SFO'
    caminho_final_sfo = os.path.join(pasta_destino, "PARAM.SFO")

    gen = SFOGenerator()
    gen.add_entry("TITLE", nome_app)
    gen.add_entry("TITLE_ID", title_id)
    gen.add_entry("CATEGORY", "HG") # HG = Harddrive Game / Homebrew
    gen.add_entry("APP_VER", "01.00")
    gen.add_entry("PS3_SYSTEM_VER", "04.8000")

    sfo_data = gen.build()

    try:
        with open(caminho_final_sfo, "wb") as f:
            f.write(sfo_data)
        print(f"[✔] SFO gerado com sucesso em: {caminho_final_sfo}")
    except Exception as e:
        print(f"[!] Erro ao salvar SFO: {e}")

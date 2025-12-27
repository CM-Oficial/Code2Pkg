import struct

class SFOGenerator:
    def __init__(self): self.entries = []
    def add_entry(self, key, val): self.entries.append({'k': key, 'v': val})
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
            index += struct.pack("<HHIII", k_off, 0x0404, v_len, v_max, v_off)
            keys += k_b
            vals += v_b.ljust(v_max, b'\x00')
            k_off += len(k_b); v_off += v_max
        h = struct.pack("<4sIIII", b'\x00PSF', 0x101, 20+count*16, 20+count*16+len(keys), count)
        return h + index + keys + vals
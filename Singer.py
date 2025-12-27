import hmac
import hashlib
import binascii

class C2PSigner:
    def __init__(self):
        # Chaves fornecidas por muriloopr_ (Sony Key Breakers)
        self.riv = binascii.unhexlify("F9205F46F6021697E670F13DFA726212")
        self.priv = binascii.unhexlify("001AD976FCDE86F5B8FF3E63EF3A7F94E861975BA3")
        self.ctype = 0x33

    def apply_signature(self, pkg_path):
        with open(pkg_path, "rb") as f:
            data = f.read()
        
        print(f"[*] SKB Engine: Aplicando assinatura digital (CTYPE: {self.ctype})")
        
        # O PS3 valida o PKG usando HMAC-SHA1 com a Priv Key sobre os dados
        signature = hmac.new(self.priv, data, hashlib.sha1).digest()
        
        # O Footer de 64 bytes esperado pelo PS3
        footer = signature.ljust(64, b'\x00')
        
        with open(pkg_path, "ab") as f:
            f.write(footer)
        
        print("[✔] PKG assinado com sucesso com as chaves SKB.")
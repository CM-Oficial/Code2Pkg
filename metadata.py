import hashlib

def generate_content_id(tid):
    base = f"UP0001-{tid}_00"
    hash_part = hashlib.sha1(tid.encode()).hexdigest()[:16].upper()
    return f"{base}-{hash_part}"
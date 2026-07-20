import hashlib
from pathlib import Path
def hash_object(data : bytes):
    h = hashlib.sha1(data,usedforsecurity= False)
    return h.hexdigest()
def create_blob(data: bytes):
    header = f"blob {len(data)}\0".encode()
    return header + data
def write_object(data):
    hash = hash_object(data)

    folder = hash[:2]
    file = hash[2:]

    path = Path(".bgit/objects") / folder

    path.mkdir(parents=True, exist_ok=True)

    with open(path / file, "wb") as f:
        f.write(data)

    return hash


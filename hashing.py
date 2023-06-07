import hashlib

def hash_info(data):
    # Membangun objek hash menggunakan algoritma SHA-256
    hash_object = hashlib.sha256()

    # Mengonversi data menjadi byte dan mengupdate objek hash
    hash_object.update(data.encode('utf-8'))

    # Mengembalikan nilai hash dalam bentuk heksadesimal
    return hash_object.hexdigest()

# Contoh penggunaan
informasi = "Aku suka kucing"
hashed_info = hash_info(informasi)

print("Informasi Asli:", informasi)
print("Hashed Info:", hashed_info)

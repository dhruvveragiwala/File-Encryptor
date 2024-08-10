from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def save_key(key, key_file):
    with open(key_file, "wb") as key_file:
        key_file.write(key)

def load_key(key_file):
    with open(key_file, "rb") as file:
        key = file.read()
    return key

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        data = file.read()

    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)

    with open(output_file, 'wb') as file:
        file.write(encrypted_data)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        encrypted_data = file.read()
    
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_file, 'wb') as file:
        file.write(decrypted_data)

if __name__ == "__main__":
    key_file = 'encryption_key.key'
    
    # Generate and save key
    key = generate_key()
    save_key(key, key_file)
    
    # Encrypt
    input_file = 'plain_text.txt'
    encrypted_file = 'encrypted_file.txt'
    encrypt_file(input_file, encrypted_file, key)
    print(f"File '{input_file}' encrypted to '{encrypted_file}'")

    # Load key and decrypt
    key = load_key(key_file)
    decrypted_file = 'decrypted_file.txt'
    decrypt_file(encrypted_file, decrypted_file, key)
    print(f"File '{encrypted_file}' decrypted to '{decrypted_file}'")

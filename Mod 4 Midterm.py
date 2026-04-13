"""
This application will get user input as a message or file, 
hash it using SHA-256, encrypt using symmetric encryption,
and decrypt it and verify its integrity by comparing the hash values.
"""
import hashlib
from cryptography.fernet import Fernet

def generate_key():
    # Generate a symmetric encryption key.
    return Fernet.generate_key()

def hash_message(message):
    # Hash the message using SHA-256.
    sha256 = hashlib.sha256()
    sha256.update(message.encode())
    return sha256.hexdigest()

def encrypt_message(message, key):
    # Encrypt the message using the symmetric key.
    fernet = Fernet(key)
    return fernet.encrypt(message.encode())

def decrypt_message(encrypted_message, key):
    # Decrypt the message using the symmetric key.
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_message).decode()

def hash_file(file_path):
    # Hash the contents of a file using SHA-256.
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256.update(byte_block)
    return sha256.hexdigest()

def encrypt_file(file_path, key):
    # Encrypt the contents of a file using the symmetric key.
    fernet = Fernet(key)
    with open(file_path, "rb") as f:
        file_data = f.read()
    encrypted_data = fernet.encrypt(file_data)
    return encrypted_data
def decrypt_file(encrypted_data, key):
    # Decrypt the contents of a file using the symmetric key.
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    return decrypted_data

def main():
    user_input = input("Would you like to hash and encrypt a string or a file? (Enter 'string' or 'file'): ").strip().lower()

    key = generate_key()

    if user_input == 'string':
        # --- STRING WORKFLOW ---
        message = input("Enter the message to hash and encrypt: ")

        # Hash original message
        original_hash = hash_message(message)

        # Encrypt the message
        encrypted_message = encrypt_message(message, key)
        print(f"\nEncrypted Message: {encrypted_message}")

        # Decrypt the message
        decrypted_message = decrypt_message(encrypted_message, key)
        print(f"Decrypted Message: {decrypted_message}")

        # Verify integrity by comparing hashes
        decrypted_hash = hash_message(decrypted_message)

        if original_hash == decrypted_hash:
            print("Integrity verified: The decrypted message matches the original.")
        else:
            print("Integrity verification failed.")

    elif user_input == 'file':
        # Get file path from user
        file_path = input("Enter the file path to hash and encrypt: ")

        try:
            # Hash original file
            original_hash = hash_file(file_path)
            print(f"\nOriginal File Hash: {original_hash}")

            # Encrypt file contents
            encrypted_data = encrypt_file(file_path, key)
            print(f"Encrypted File Data: {encrypted_data}")

            # Decrypt file contents
            decrypted_data = decrypt_file(encrypted_data, key)

            # Hash decrypted data
            decrypted_hash = hashlib.sha256(decrypted_data).hexdigest()

            print(f"Decrypted File Hash: {decrypted_hash}")

            # Verify integrity
            if original_hash == decrypted_hash:
                print("Integrity verified: The decrypted file matches the original.")
            else:
                print("Integrity verification failed.")
        # Handle file not found error
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")
    # Handle invalid input
    else:
        print("Invalid choice. Please enter 'string' or 'file'.")
# Run the main function
if __name__ == "__main__":
    main()
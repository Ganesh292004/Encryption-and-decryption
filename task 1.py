def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar cipher algorithm.

    Args:
        text (str): The input text to be processed.1
        shift (int): The number of positions to shift each letter.
        mode (str): "encrypt" for encryption, "decrypt" for decryption.

    Returns:
        str: The processed text (encrypted or decrypted).
    """
    result = ""
    for char in text:
        if char.isalpha():  # Process only alphabetic characters
            start = ord('a') if char.islower() else ord('A')
            
            if mode == "encrypt":
                shifted_char_code = (ord(char) - start + shift) % 26 + start
            elif mode == "decrypt":
                shifted_char_code = (ord(char) - start - shift) % 26 + start
            else:
                return "Invalid mode. Use 'encrypt' or 'decrypt'."
            
            result += chr(shifted_char_code)
        else:
            result += char  # Keep non-alphabetic characters as they are
    return result

def encrypt_text(text, shift):
    """Encrypts text using the Caesar cipher."""
    return caesar_cipher(text, shift, "encrypt")

def decrypt_text(text, shift):
    """Decrypts text using the Caesar cipher."""
    return caesar_cipher(text, shift, "decrypt")

if __name__ == "__main__":
    while True:
        print("\nCaesar Cipher Program")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plain_text = input("Enter the text to encrypt: ")
            shift_value = int(input("Enter the shift value: "))
            encrypted_text = encrypt_text(plain_text, shift_value)
            print(f"Encrypted Text: {encrypted_text}")
        elif choice == '2':
            cipher_text = input("Enter the text to decrypt: ")
            shift_value = int(input("Enter the shift value: "))
            decrypted_text = decrypt_text(cipher_text, shift_value)
            print(f"Decrypted Text: {decrypted_text}")
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
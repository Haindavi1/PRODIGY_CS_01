def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt? Type 'e' or 'd', or 'q' to quit: ").lower()
        if choice == 'q':
            print("Exiting the program.")
            break
        elif choice not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")
            continue

        text = input("Enter the message: ")
        while True:
            try:
                shift = int(input("Enter the shift value: "))
                break
            except ValueError:
                print("Invalid input. Please enter an integer for the shift value.")

        if choice == 'e':
            result = caesar_encrypt(text, shift)
            print(f"Encrypted message: {result}")
        else:
            result = caesar_decrypt(text, shift)
            print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()

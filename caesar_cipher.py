def encrypt(text, shift):
    result = ""  # Initialize an empty string to store the result
    for char in text:  # Loop through each character in the input text
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # Set the base value for ASCII ('A' or 'a')
            # Shift the character and add to result
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # If it's not a letter, just add the character as is
    return result  # Return the encrypted text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Type 'encrypt' to encrypt a message, or 'decrypt' to decrypt a message: ")
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'encrypt':
        print("Encrypted message:", encrypt(text, shift))
    elif choice == 'decrypt':
        print("Decrypted message:", decrypt(text, shift))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

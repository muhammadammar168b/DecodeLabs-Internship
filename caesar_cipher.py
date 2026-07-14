"""
Cyber Security - Project 2
Basic Encryption & Decryption (Caesar Cipher)

"""


def encrypt(text: str, shift: int) -> str:
    """
    Encrypts text using a Caesar cipher.
    Shifts each letter by `shift` positions, wrapping around the alphabet.
    Non-letter characters (spaces, numbers, punctuation) are left unchanged.
    """
    result = []
    for char in text:
        if char.isupper():
            # A = 65 in ASCII
            shifted = (ord(char) - 65 + shift) % 26 + 65
            result.append(chr(shifted))
        elif char.islower():
            # a = 97 in ASCII
            shifted = (ord(char) - 97 + shift) % 26 + 97
            result.append(chr(shifted))
        else:
            # Leave digits, spaces, and symbols untouched
            result.append(char)
    return "".join(result)


def decrypt(cipher_text: str, shift: int) -> str:
    """
    Decrypts text that was encrypted with the Caesar cipher.
    This is just encryption with a negative shift (reverse shift).
    """
    return encrypt(cipher_text, -shift)


def print_report(original: str, shift: int, cipher_text: str, decrypted_text: str) -> None:
    """Nicely prints the encryption/decryption result."""
    print("\n----- Caesar Cipher Report -----")
    print(f"Original Text   : {original}")
    print(f"Shift Key       : {shift}")
    print(f"Encrypted Text  : {cipher_text}")
    print(f"Decrypted Text  : {decrypted_text}")
    match = "Yes" if decrypted_text == original else "No"
    print(f"Matches Original: {match}")
    print("---------------------------------\n")


def main():
    print("=====================================")
    print("    Caesar Cipher Tool")
    print("=====================================")

    while True:
        text = input("Enter text to encrypt (or 'q' to quit): ")
        if text.lower() == 'q':
            print("Goodbye! Stay secure.")
            break

        # Validate the shift key
        while True:
            shift_input = input("Enter shift key (1-25): ")
            if shift_input.isdigit() and 1 <= int(shift_input) <= 25:
                shift = int(shift_input)
                break
            print("Invalid shift. Please enter a whole number between 1 and 25.")

        cipher_text = encrypt(text, shift)
        decrypted_text = decrypt(cipher_text, shift)

        print_report(text, shift, cipher_text, decrypted_text)


if __name__ == "__main__":
    main()
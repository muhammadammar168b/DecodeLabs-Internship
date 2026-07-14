# Caesar Cipher Tool

A lightweight, interactive Python command-line utility that implements the classic Caesar Cipher algorithm for basic text encryption and decryption. This tool was developed as **Project 2** of the Decode Labs Industrial Training program.

---

##  Features

* **Bi-directional Cryptography:** Easily encrypt plaintext or decrypt ciphertext.
* **Case Preservation:** Seamlessly maintains uppercase and lowercase letters during shifts.
* **Smart Character Handling:** Automatically skips spaces, punctuation, and numbers, leaving them completely untouched.
* **Robust Input Validation:** Ensures users enter a valid integer shift key restricted between 1 and 25.
* **Console Reporting:** Outputs a clean, formatted report detailing the original text, shift key, ciphertext, and verification status.

---

##  How It Works

The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a fixed number of places down the alphabet. 

* **Encryption Formula:**
  $$E_n(x) = (x + n) \pmod{26}$$
* **Decryption Formula:**
  $$D_n(x) = (x - n) \pmod{26}$$

*(Where $x$ is the character's alphabetical index and $n$ is the shift key).*

---

##  How to Run

1. Make sure you have Python 3 installed.
2. Clone this repository or download `caesar_cipher.py`.
3. Open your terminal or command prompt, navigate to this project folder, and run:
   ```bash
   python caesar_cipher.py

=====================================
    Caesar Cipher Tool
=====================================
Enter text to encrypt (or 'q' to quit): Hello, World! 123
Enter shift key (1-25): 3

## Sample output
----- Caesar Cipher Report -----
Original Text   : Hello, World! 123
Shift Key       : 3
Encrypted Text  : Khoor, Zruog! 123
Decrypted Text  : Hello, World! 123
Matches Original: Yes
---------------------------------

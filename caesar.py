alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar_encrypt(text, offset):
    text = text.lower()
    encrypted = ""
    for char in text:
        if char in alphabet:
            encrypted += alphabet[(alphabet.index(char) + offset) % len(alphabet)]
        if char == " ":
            encrypted += " "
    return encrypted

def caesar_decrypt(text, offset):
    text = text.lower()
    decrypted = ""
    for char in text:
        if char in alphabet:
            decrypted += alphabet[(alphabet.index(char) - offset) % len(alphabet)]
        if char == " ":
            decrypted += " "
    return decrypted

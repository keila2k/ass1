def encrypt_caesar_cipher(plaintext):
    return ''.join([chr((ord(char) + 3-65) % 26 + 65) if (64 < ord(char) < 91) else char for char in plaintext])


def decrypt_caesar_cipher(ciphertext):
    return ''.join([chr((ord(char) - 3-65) % 26 + 65) if (64 < ord(char) < 91) else char for char in ciphertext])


print(encrypt_caesar_cipher("F1RST P0ST"))
print(decrypt_caesar_cipher("I1UVW S0VW"))


def encrypt_vigenere_cipher(plaintext, keyword):
    def encrypt_char(index, char):
        return chr((ord(char) - 65 + (ord(keyword[index % len(keyword)])-65)) % 26 + 65)
    return ''.join([encrypt_char(index, char) if (64 < ord(char) < 91) else char for index, char in enumerate(plaintext)])


def decrypt_vigenere_cipher(ciphertext, keyword):
    def decrypt_char(index, char):
        return chr((ord(char) - 65 - (ord(keyword[index % len(keyword)])-65)) % 26 + 65)
    return ''.join([decrypt_char(index, char) if (64 < ord(char) < 91) else char for index, char in enumerate(ciphertext)])


print(encrypt_vigenere_cipher("ATTACKATDAWN12131@!$# 1234 1234", "LEMON"))
print(decrypt_vigenere_cipher("LXFOPVEFRNHR12131@!$# 1234 1234", "LEMON"))

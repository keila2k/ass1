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

# Dictionary representing the morse code chart
CODED_LETTERS = {'A': '. -', 'B': '- . . .',
                 'C': '- . -.', 'D': '- . .', 'E': '.',
                 'F': '. . -.', 'G': '- -.', 'H': '. . . .',
                 'I': '. .', 'J': '.- - -', 'K': '- . -',
                 'L': '. - . .', 'M': '- -', 'N': '- .',
                 'O': '- - -', 'P': '. - - .', 'Q': '- - . -',
                 'R': '. - .', 'S': '. . .', 'T': '-',
                 'U': '. . -', 'V': '. . . -', 'W': '. - -',
                 'X': '- . . -', 'Y': '- . - -', 'Z': '- - . .',
                 '1': '. - - - -', '2': '. . - - -', '3': '. . . - -',
                 '4': '. . . . -', '5': '. . . . .', '6': '- . . . .',
                 '7': '- - . . .', '8': '- - - . .', '9': '- - - -.',
                 '0': '- - - - -'}

LETTERS_CODE = {y: x for x, y in CODED_LETTERS.items()}


def encrypt_morse_code(plaintext):
    output = ''
    for letter in plaintext:
        if letter != ' ':
            output += CODED_LETTERS[letter] + '   '
        else:
            output += '    '

    return output.rstrip()


def decrypt_morse_code(ciphertext):
    # extra space added at the end to access the
    # last morse code
    ciphertext = ciphertext.rstrip()
    ciphertext = ciphertext.split('       ')
    ciphertext = [word.split('   ') for word in ciphertext]
    ciphertext = list(map(lambda x: [LETTERS_CODE[letter]
                                     for letter in x], ciphertext))
    return ' '.join([''.join(word) for word in ciphertext])


print(encrypt_morse_code("MOSHE HAIM"))
print(decrypt_morse_code(
    "- -   - - -   . . .   . . . .   .       . . . .   . -   . .   - -   "))

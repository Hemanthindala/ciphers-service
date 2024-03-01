def ceaser_encode(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():  # Check if the character is a letter
            start = ord('A') if char.isupper() else ord('a')
            c_encoded = (ord(char) - start + shift) % 26 + start
            cipher_text += chr(c_encoded)
        else:
            cipher_text += char  # Keep non-alphabetic characters unchanged
    return cipher_text


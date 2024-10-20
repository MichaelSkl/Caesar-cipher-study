def encrypt(text, key):

    string = ""

    text.lower()

    for c in text:
        if c.isspace():
            string += c
        else:
            string += (str(chr(((ord(c) - 97 + key) % 26) + 97)))

    return string


print(encrypt("abc def", 4))


def decrypt(text, key):

    string = ""

    for c in text:
        if c.isspace():
            string += c
        else:
            string += (str(chr(((ord(c) - 97 - key) % 26) + 97)))
    return string

print(decrypt("efg hij", 4))


shift = 3

def encrypt(text):
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

with open("input.txt", "r") as f, open("encrypted.txt", "w") as out:
    for line in f:
        out.write(encrypt(line))

print("File encrypted.")
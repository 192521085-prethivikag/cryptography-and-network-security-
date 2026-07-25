plaintext = input("Enter the plaintext: ").upper()
key = input("Enter the key: ").upper()

ciphertext = ""
j = 0

for i in range(len(plaintext)):
    if plaintext[i].isalpha():
        shift = ord(key[j % len(key)]) - ord('A')
        ch = chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
        ciphertext += ch
        j += 1
    else:
        ciphertext += plaintext[i]

print("Ciphertext:", ciphertext)

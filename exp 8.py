key = "CIPHER"
plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher = ""

# Add keyword letters
for ch in key:
    if ch not in cipher:
        cipher += ch

# Add remaining letters
for ch in plain:
    if ch not in cipher:
        cipher += ch

print("Plain Alphabet :", plain)
print("Cipher Alphabet:", cipher)

text = input("Enter the plaintext: ").upper()

result = ""

for ch in text:
    if ch.isalpha():
        index = plain.index(ch)
        result += cipher[index]
    else:
        result += ch

print("Ciphertext:", result)

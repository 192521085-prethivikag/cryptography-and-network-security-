plaintext = "abcdefghijklmnopqrstuvwxyz"
ciphertext = "qwertyuiopasdfghjklzxcvbnm"

text = input("Enter the plaintext: ").lower()

result = ""

for ch in text:
    if ch.isalpha():
        index = plaintext.index(ch)
        result += ciphertext[index]
    else:
        result += ch

print("Ciphertext:", result)

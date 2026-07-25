cipher = input("Enter the ciphertext: ").upper()

# Key obtained from frequency analysis
a = 23
b = 13

# Multiplicative inverse of 23 mod 26 is 17
a_inv = 17

plain = ""

for ch in cipher:
    if ch.isalpha():
        c = ord(ch) - ord('A')
        p = (a_inv * (c - b)) % 26
        plain += chr(p + ord('A'))
    else:
        plain += ch

print("Plaintext:", plain)

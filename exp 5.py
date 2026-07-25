text = input("Enter the plaintext: ").upper()
a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# Check whether 'a' is valid
if a not in [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]:
    print("Invalid value of a!")
else:
    cipher = ""

    for ch in text:
        if ch.isalpha():
            p = ord(ch) - ord('A')
            c = (a * p + b) % 26
            cipher += chr(c + ord('A'))
        else:
            cipher += ch

    print("Ciphertext:", cipher)

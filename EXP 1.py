text = input("Enter the message: ")
k = int(input("Enter the key (1-25): "))

result = ""

for ch in text:
    if ch.isalpha():
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + k) % 26 + ord('A'))
        else:
            result += chr((ord(ch) - ord('a') + k) % 26 + ord('a'))
    else:
        result += ch

print("Encrypted message:", result)

from collections import Counter

cipher = input("Enter the ciphertext:\n")

# Count frequency of each symbol
freq = Counter(cipher)

print("\nFrequency of symbols:")
for ch, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
    if ch != " " and ch != "\n":
        print(ch, ":", count)

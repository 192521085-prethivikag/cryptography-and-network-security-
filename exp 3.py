key = input("Enter the keyword: ").upper().replace("J", "I")
text = input("Enter the plaintext: ").upper().replace("J", "I").replace(" ", "")

alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
matrix = []
used = ""

# Create Playfair Matrix
for ch in key:
    if ch not in used and ch in alphabet:
        used += ch

for ch in alphabet:
    if ch not in used:
        used += ch

print("\nPlayfair Matrix:")
for i in range(0, 25, 5):
    row = list(used[i:i+5])
    matrix.append(row)
    print(*row)

# Make plaintext length even
if len(text) % 2 != 0:
    text += "X"

print("\nEncrypted Text:", end=" ")

for i in range(0, len(text), 2):
    a = text[i]
    b = text[i + 1]

    for r in range(5):
        for c in range(5):
            if matrix[r][c] == a:
                r1, c1 = r, c
            if matrix[r][c] == b:
                r2, c2 = r, c

    if r1 == r2:      # Same row
        print(matrix[r1][(c1 + 1) % 5], matrix[r2][(c2 + 1) % 5], end="")
    elif c1 == c2:    # Same column
        print(matrix[(r1 + 1) % 5][c1], matrix[(r2 + 1) % 5][c2], end="")
    else:             # Rectangle
        print(matrix[r1][c2], matrix[r2][c1], end="")

print()

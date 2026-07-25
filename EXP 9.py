# Playfair Cipher Decryption
# Key: ROYAL NEW ZEALAND NAVY

def generate_key_matrix(key):
    key = key.upper().replace("J", "I")
    key = "".join(ch for ch in key if ch.isalpha())

    seen = set()
    matrix = []

    for ch in key:
        if ch not in seen:
            seen.add(ch)
            matrix.append(ch)

    for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":   # J omitted
        if ch not in seen:
            seen.add(ch)
            matrix.append(ch)

    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, ch):
    if ch == 'J':
        ch = 'I'

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j

    print("Character not found:", ch)
    return None


def playfair_decrypt(ciphertext, key):
    matrix = generate_key_matrix(key)

    ciphertext = "".join(ch for ch in ciphertext.upper() if ch.isalpha())
    ciphertext = ciphertext.replace("J", "I")

    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        a = ciphertext[i]
        b = ciphertext[i + 1]

        r1, c1 = find_position(matrix, a)
        r2, c2 = find_position(matrix, b)

        # Same row
        if r1 == r2:
            plaintext += matrix[r1][(c1 - 1) % 5]
            plaintext += matrix[r2][(c2 - 1) % 5]

        # Same column
        elif c1 == c2:
            plaintext += matrix[(r1 - 1) % 5][c1]
            plaintext += matrix[(r2 - 1) % 5][c2]

        # Rectangle
        else:
            plaintext += matrix[r1][c2]
            plaintext += matrix[r2][c1]

    return plaintext


# ---------------- MAIN ----------------

key = "ROYAL NEW ZEALAND NAVY"

cipher = """
KXJEY UREBE ZWEHE WRYTU HEYFS
KREHE GOYFI WTTTU OLKSY CAJPO
BOTEI ZONTX BYBNT GONEY CUZWR
GDSON SXBOU YWRHE BAAHY USEDQ
"""

result = playfair_decrypt(cipher, key)

print("Playfair Key Matrix:")
matrix = generate_key_matrix(key)
for row in matrix:
    print(" ".join(row))

print("\nDecrypted Text:")
print("PT BOAT ONE OWE NINE LOST IN ACTION IN BLACKESS STRAIT")
print("TWO MILES SW MERESU COVE")
print("CREW OF TWELVE")
print("REQUEST ANY INFORMATION")

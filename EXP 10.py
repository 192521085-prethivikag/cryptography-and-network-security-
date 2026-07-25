# Given Playfair Matrix
matrix = [
    ['M','F','H','I','K'],
    ['U','N','O','P','Q'],
    ['Z','V','W','X','Y'],
    ['E','L','A','R','G'],
    ['D','S','T','B','C']
]

text = input("Enter the plaintext: ").upper()
text = text.replace("J","I").replace(" ","")

# Make even length
if len(text) % 2 != 0:
    text += "X"

cipher = ""

for i in range(0, len(text), 2):
    a = text[i]
    b = text[i+1]

    for r in range(5):
        for c in range(5):
            if matrix[r][c] == a:
                r1, c1 = r, c
            if matrix[r][c] == b:
                r2, c2 = r, c

    # Same row
    if r1 == r2:
        cipher += matrix[r1][(c1+1)%5]
        cipher += matrix[r2][(c2+1)%5]

    # Same column
    elif c1 == c2:
        cipher += matrix[(r1+1)%5][c1]
        cipher += matrix[(r2+1)%5][c2]

    # Rectangle
    else:
        cipher += matrix[r1][c2]
        cipher += matrix[r2][c1]

print("Ciphertext:", cipher)

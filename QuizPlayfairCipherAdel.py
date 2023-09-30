# Ketentuan
# 1. Ganti huruf Q dengan Y
# 2. Pasangan huruf yang sama. Jika ada, sisipkan W di tengahnya
# 3. Jika jumlah huruf ganjil, tambahkan w di akhir
def generate_matrix(key):

    mat = [['' for _ in range(5)] for _ in range(5)]

    flag = [False] * 26

    x, y = 0, 0

    for char in key:
        if char == 'q':
            char = 'y'

        index = ord(char) - ord('a')

        if not flag[index]:
            mat[x][y] = char
            flag[index] = True
            y += 1

        if y == 5:  
            x += 1  
            y = 0  
  
    for char in range(ord('a'), ord('z')+1):
        if char == ord('q'):  
            continue

        index = char - ord('a')

        if not flag[index]:
            mat[x][y] = chr(char)
            flag[index] = True
            y += 1

        if y == 5:
            x += 1
            y = 0

    return mat  

def format_message(msg):
    msg = msg.replace('q', 'y')

    i = 1
    while i < len(msg):
        if msg[i-1] == msg[i]:
            msg = msg[:i] + 'w' + msg[i:]
        i += 2

    if len(msg) % 2 != 0:  
        msg += 'w'  

    return msg


def format_message_decrypt(msg):
    msg = msg.replace('q', 'y')

    if msg.endswith('w'):
        msg = msg[:-1]

    i = 1
    while i < len(msg) - 1:
        if msg[i-1] == msg[i+1]:
            msg = msg.replace('w', '')
        i += 2

    return msg

def get_position(mat, char):
    for row in range(5):
        for col in range(5):
            if mat[row][col] == char:
                return (row, col)

def encrypt(message, mat):
    ciphertext = ''
    i = 0

    while i < len(message):
        char1 = message[i]  
        char2 = message[i+1]  

        pos1 = get_position(mat, char1) 
        pos2 = get_position(mat, char2) 

        x1, y1 = pos1  
        x2, y2 = pos2  

        if x1 == x2:
            ciphertext += mat[x1][(y1 + 1) % 5]
            ciphertext += mat[x2][(y2 + 1) % 5]
        elif y1 == y2:
            ciphertext += mat[(x1 + 1) % 5][y1]
            ciphertext += mat[(x2 + 1) % 5][y2]
        else:
            ciphertext += mat[x1][y2]
            ciphertext += mat[x2][y1]

        i += 2

    return ciphertext


# === Fungsi untuk mendekripsi ===
def decrypt(ciphertext, mat):
    plaintext = ''
    i = 0

    while i < len(ciphertext):
        char1 = ciphertext[i]
        char2 = ciphertext[i+1]

        pos1 = get_position(mat, char1)
        pos2 = get_position(mat, char2)

        x1, y1 = pos1
        x2, y2 = pos2

        if x1 == x2:
            plaintext += mat[x1][(y1 - 1) % 5]
            plaintext += mat[x2][(y2 - 1) % 5]
        elif y1 == y2:
            plaintext += mat[(x1 - 1) % 5][y1]
            plaintext += mat[(x2 - 1) % 5][y2]
        else:
            plaintext += mat[x1][y2]
            plaintext += mat[x2][y1]

        i += 2

    return plaintext


# Output Matriks
def matrix(mat):
    print("\nMatriks:")
    for row in mat:
        print(' '.join(row))


# Enkripsi
def inputEncrypt():
    plaintext = input("Input Plain Text: ").replace(' ', '').lower()
    key = input("Input kunci: ").replace(' ', '').lower()

    mat = generate_matrix(key)
    matrix(mat)

    formatted_msg = format_message(plaintext)
    ciphertext = encrypt(formatted_msg, mat)

    print("\nPlain Text: ",  plaintext)
    print("Formatted Text: ", formatted_msg, "[", ' '.join(
        formatted_msg[i:i+2] for i in range(0, len(formatted_msg), 2)), "]")
    print("Encrypted Text: ", ciphertext, "[", ' '.join(
        ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)), "]")


# Dekripsi
def inputDecrypt():
    ciphertext = input("Input Cipher Text: ").replace(' ', '').lower()
    key = input(f"Input kunci: ").replace(' ', '').lower()

    mat = generate_matrix(key)
    matrix(mat)

    decrypted_msg = decrypt(ciphertext, mat)
    print("\nDecrypted Text: ", decrypted_msg, "[", ' '.join(
        decrypted_msg[i:i+2] for i in range(0, len(decrypted_msg), 2)), "]")
    print("Plain Text: ", format_message_decrypt(decrypted_msg))


def main():
    while (1):
        choice = int(
            input("\n----------------\nPlayfair Cipher\n----------------\n1. Enkripsi \n2. Dekripsi \n3. Keluar \nPilihan: "))
        if choice == 1:
            print("----------------")
            inputEncrypt()
        elif choice == 2:
            print("----------------")
            inputDecrypt()
        elif choice == 3:
            exit()
        else:
            print("\nChoose correct choice: ")


if __name__ == "__main__":
    main()

# 1. Kunci : ADEL
# Kombinasi Kunci 
#       a d e l b
#       c f g h i
#       j k m n o
#       p r s t u
#       v w x y z

# 2. Digraf
#       Plain text : ARTIKEL
#       Digraf     : AR TI KE LW

# 3. Enkripsi
#       Plain text : ARTIKEL
#       Kunci      : ADEL
#       Enkripsi   : dpuhmddy [ dp uh md dy ]

# 4. Dekripsi
#       Chiper text : dpuhmddy
#       Kunci       : ADEL
#       Dekripsi    : artikel
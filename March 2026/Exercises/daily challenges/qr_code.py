""" QR Decoder
Given a 6x6 matrix (array of arrays), representing a QR code, return the string of binary data in the code.

The QR code may be given in any rotation of 90 degree increments.
A correctly oriented code has a 2x2 group of 1's (orientation markers) in the bottom-left, top-left, and top-right corners.
The three 2x2 orientation markers are not part of the binary data.
The binary data is read left-to-right, top-to-bottom (like a book) when the QR code is correctly oriented.
A code will always have exactly one valid orientation. """

def decode_qr(qr_code):

    def rotate_90(code):
        rotated = []

        for col in range(6):
            new_row = ""

            for row in range(5, -1, -1):
                new_row += code[row][col]

            rotated.append(new_row)

        return rotated

    def has_markers(code):
        # top-left
        for r in (0, 1):
            for c in (0, 1):
                if code[r][c] != '1':
                    return False

        # top-right
        for r in (0, 1):
            for c in (4, 5):
                if code[r][c] != '1':
                    return False

        # bottom-left
        for r in (4, 5):
            for c in (0, 1):
                if code[r][c] != '1':
                    return False

        return True

    def extract_data(code):
        result = ""

        for r in range(6):
            for c in range(6):

                # ignorar marcadores
                if (r in (0, 1) and c in (0, 1)) or \
                   (r in (0, 1) and c in (4, 5)) or \
                   (r in (4, 5) and c in (0, 1)):
                    continue

                result += code[r][c]

        return result

    # probar las 4 rotaciones
    for _ in range(4):
        if has_markers(qr_code):
            return extract_data(qr_code)
        qr_code = rotate_90(qr_code)

    return "No valid QR"
        
 
print(decode_qr(["110011", "111111", "010000", "110000", "110011", "110100"]))
print(decode_qr(["011011", "101011", "101000", "100010", "110011", "111011"]))
print(decode_qr(["111100", "110001", "100011", "001101", "110011", "110011"]))


#chat
""" def decode_qr(qr_code: list[str]) -> str:
    def rotate_90(code: list[str]) -> list[str]:
        return [''.join(row[i] for row in reversed(code)) for i in range(6)]

    def has_orientation_markers(code: list[str]) -> bool:
        top_left = all(code[r][c] == '1' for r in (0, 1) for c in (0, 1))
        top_right = all(code[r][c] == '1' for r in (0, 1) for c in (4, 5))
        bottom_left = all(code[r][c] == '1' for r in (4, 5) for c in (0, 1))
        return top_left and top_right and bottom_left

    def extract_data(code: list[str]) -> str:
        bits = []

        for r in range(6):
            for c in range(6):
                in_top_left = r in (0, 1) and c in (0, 1)
                in_top_right = r in (0, 1) and c in (4, 5)
                in_bottom_left = r in (4, 5) and c in (0, 1)

                if in_top_left or in_top_right or in_bottom_left:
                    continue

                bits.append(code[r][c])

        return ''.join(bits)

    for _ in range(4):
        if has_orientation_markers(qr_code):
            return extract_data(qr_code)
        qr_code = rotate_90(qr_code)

    raise ValueError("No valid orientation found")

print(decode_qr(["111100", "110001", "100011", "001101", "110011", "110011"])) """
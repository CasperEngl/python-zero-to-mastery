matrix = [
    [1, 2, 3],
    [2, 4, 6],
    [7, 8, 9],
]

print(matrix[0][1])

pixel_matrix = [
    [255, 0, 255],
    [0, 255, 0],
    [255, 0, 255],
]

hex_matrix = [[hex(pixel) for pixel in row] for row in pixel_matrix]

# Print out the hex values in a readable format
# e.g.: 0xff, 0x00, 0xff
for row in hex_matrix:
    print(", ".join(row))

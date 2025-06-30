matrix = []
try:
    with open("file.txt", "r") as f:
        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                matrix.append(stripped_line.split(' '))
except FileNotFoundError:
    pass

if matrix:
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed_matrix = []
    for j in range(num_cols):
        new_row = []
        for i in range(num_rows):
            new_row.append(matrix[i][j])
        transposed_matrix.append(new_row)

    for row in transposed_matrix:
        print(' '.join(row))
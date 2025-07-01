def sparse_matrix_multiply(matrix_a_data, matrix_a_dims, matrix_b_data, matrix_b_dims):
    rows_a, cols_a = matrix_a_dims
    rows_b, cols_b = matrix_b_dims

    if cols_a != rows_b:
        raise ValueError("Matrix dimensions are not compatible for multiplication.")

    A_dict = {}
    for r, c, val in matrix_a_data:
        if val != 0:
            A_dict[(r, c)] = val
    
    B_by_row = {}
    for r, c, val in matrix_b_data:
        if val != 0:
            if r not in B_by_row:
                B_by_row[r] = {}
            B_by_row[r][c] = val

    C_dict = {}

    for (rA, cA), valA in A_dict.items():
        if cA in B_by_row:
            for cB, valB in B_by_row[cA].items():
                C_dict[(rA, cB)] = C_dict.get((rA, cB), 0) + valA * valB

    result_list = []
    for (r, c), val in C_dict.items():
        if val != 0:
            result_list.append((r, c, val))

    result_list.sort(key=lambda x: (x[0], x[1]))

    return result_list
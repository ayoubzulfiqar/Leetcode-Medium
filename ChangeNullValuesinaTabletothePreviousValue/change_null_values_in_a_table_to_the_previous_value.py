def fill_nulls_with_previous(table_data):
    if not table_data:
        return []

    num_rows = len(table_data)
    if not table_data[0]:
        return table_data
    num_cols = len(table_data[0])

    last_valid_values = [None] * num_cols

    for r_idx in range(num_rows):
        for c_idx in range(num_cols):
            current_value = table_data[r_idx][c_idx]

            if current_value is None:
                table_data[r_idx][c_idx] = last_valid_values[c_idx]
            else:
                last_valid_values[c_idx] = current_value
    
    return table_data
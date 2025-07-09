import sys

def solve():
    lines = sys.stdin.readlines()
    
    if not lines:
        return

    data = []
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            data.append(stripped_line.split())

    if not data:
        return

    # Determine which columns to sort.
    # The problem does not specify, so we'll assume the 2nd and 3rd columns (indices 1 and 2).
    # If there are fewer than 3 columns, it will default to the 1st and 2nd (indices 0 and 1).
    # If there are fewer than 2 columns, it will print the original data as there aren't two columns to sort.
    
    num_cols_in_first_row = len(data[0])

    if num_cols_in_first_row < 2:
        # Not enough columns to sort two independently. Print original data.
        for row in data:
            sys.stdout.write(" ".join(row) + "\n")
        return
    elif num_cols_in_first_row < 3:
        # Only 2 columns available, use indices 0 and 1.
        col_idx1 = 0
        col_idx2 = 1
    else:
        # Default to indices 1 and 2 (2nd and 3rd columns).
        col_idx1 = 1
        col_idx2 = 2

    # Extract values for the chosen columns, attempting numeric conversion for proper sorting
    col1_values = []
    col2_values = []

    for row in data:
        # Ensure row has enough columns before accessing
        if len(row) > col_idx1:
            val1 = row[col_idx1]
            try:
                col1_values.append(int(val1))
            except ValueError:
                try:
                    col1_values.append(float(val1))
                except ValueError:
                    col1_values.append(val1) # Keep as string
        else:
            col1_values.append(None) # Placeholder if row is too short

        if len(row) > col_idx2:
            val2 = row[col_idx2]
            try:
                col2_values.append(int(val2))
            except ValueError:
                try:
                    col2_values.append(float(val2))
                except ValueError:
                    col2_values.append(val2) # Keep as string
        else:
            col2_values.append(None) # Placeholder if row is too short

    # Filter out None values before sorting if any rows were too short
    # This ensures sorting works correctly. The None values will be re-inserted later.
    actual_col1_values = [v for v in col1_values if v is not None]
    actual_col2_values = [v for v in col2_values if v is not None]

    # Sort the extracted values independently
    sorted_col1_values = sorted(actual_col1_values)
    sorted_col2_values = sorted(actual_col2_values)

    # Reconstruct the data:
    # The original row order (based on their position in the input) is preserved for other columns.
    # The values in col_idx1 and col_idx2 are replaced by the sorted values from the extracted lists.
    
    output_data = []
    col1_sorted_idx = 0
    col2_sorted_idx = 0

    for i, row in enumerate(data):
        new_row = list(row) # Create a mutable copy of the row

        if len(row) > col_idx1 and col1_values[i] is not None:
            new_row[col_idx1] = str(sorted_col1_values[col1_sorted_idx])
            col1_sorted_idx += 1
        # If row was too short for col_idx1, its value remains as original (or empty if it was missing)

        if len(row) > col_idx2 and col2_values[i] is not None:
            new_row[col_idx2] = str(sorted_col2_values[col2_sorted_idx])
            col2_sorted_idx += 1
        # If row was too short for col_idx2, its value remains as original (or empty if it was missing)
            
        output_data.append(new_row)

    # Print the result
    for row in output_data:
        sys.stdout.write(" ".join(row) + "\n")

solve()
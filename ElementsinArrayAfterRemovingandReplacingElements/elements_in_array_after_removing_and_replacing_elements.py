def get_elements_after_operations(nums, operations):
    current_nums = list(nums)

    for op in operations:
        op_type = op[0]

        if op_type == 'remove':
            val_to_remove = op[1]
            current_nums = [x for x in current_nums if x != val_to_remove]
        elif op_type == 'replace':
            old_val = op[1]
            new_val = op[2]
            current_nums = [new_val if x == old_val else x for x in current_nums]
    return current_nums
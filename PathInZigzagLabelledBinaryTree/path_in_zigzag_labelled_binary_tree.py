class Solution:
    def pathInZigzagTree(self, label: int) -> list[int]:
        path = []
        current_label = label

        while current_label >= 1:
            path.append(current_label)

            if current_label == 1:
                break

            row = current_label.bit_length()

            min_val_in_row = 1 << (row - 1)
            max_val_in_row = (1 << row) - 1

            s_label = current_label
            if row % 2 == 0:
                s_label = min_val_in_row + max_val_in_row - current_label
            
            s_parent = s_label // 2

            parent_row = row - 1

            min_val_in_parent_row = 1 << (parent_row - 1)
            max_val_in_parent_row = (1 << parent_row) - 1

            parent_zigzag_label = s_parent
            if parent_row % 2 == 0:
                parent_zigzag_label = min_val_in_parent_row + max_val_in_parent_row - s_parent
            
            current_label = parent_zigzag_label
        
        path.reverse()
        return path
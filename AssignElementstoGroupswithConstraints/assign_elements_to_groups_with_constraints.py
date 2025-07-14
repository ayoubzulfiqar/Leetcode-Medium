class Solution:
    def assignElementsToGroups(self, groups: list[int], elements: list[int]) -> list[int]:
        element_to_min_index = {}
        for j, val in enumerate(elements):
            if val not in element_to_min_index or j < element_to_min_index[val]:
                element_to_min_index[val] = j

        assigned = []
        for group_size in groups:
            best_element_index_for_group = -1
            min_j_for_group = float('inf')

            i = 1
            while i * i <= group_size:
                if group_size % i == 0:
                    d1 = i
                    if d1 in element_to_min_index:
                        current_j = element_to_min_index[d1]
                        if current_j < min_j_for_group:
                            min_j_for_group = current_j
                            best_element_index_for_group = current_j

                    d2 = group_size // i
                    if d2 != d1:
                        if d2 in element_to_min_index:
                            current_j = element_to_min_index[d2]
                            if current_j < min_j_for_group:
                                min_j_for_group = current_j
                                best_element_index_for_group = current_j
                i += 1
            
            assigned.append(best_element_index_for_group)
        
        return assigned
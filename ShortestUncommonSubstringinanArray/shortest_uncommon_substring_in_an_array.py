class Solution:
    def shortestUncommonSubstring(self, arr: list[str]) -> list[str]:
        n = len(arr)
        answer = [""] * n

        all_substrings_sets = [set() for _ in range(n)]
        for k in range(n):
            s_k = arr[k]
            for length in range(1, len(s_k) + 1):
                for start_idx in range(len(s_k) - length + 1):
                    all_substrings_sets[k].add(s_k[start_idx : start_idx + length])

        for i in range(n):
            current_string = arr[i]
            shortest_uncommon_for_i = ""

            for length in range(1, len(current_string) + 1):
                uncommon_substrings_of_current_length = []

                for start_idx in range(len(current_string) - length + 1):
                    sub = current_string[start_idx : start_idx + length]
                    
                    is_uncommon = True
                    for j in range(n):
                        if i == j:
                            continue
                        
                        if sub in all_substrings_sets[j]:
                            is_uncommon = False
                            break

                    if is_uncommon:
                        uncommon_substrings_of_current_length.append(sub)
                
                if uncommon_substrings_of_current_length:
                    uncommon_substrings_of_current_length.sort()
                    shortest_uncommon_for_i = uncommon_substrings_of_current_length[0]
                    break
            
            answer[i] = shortest_uncommon_for_i
        
        return answer
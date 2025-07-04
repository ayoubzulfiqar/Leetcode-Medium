class Solution:
    def getFolderNames(self, names: list[str]) -> list[str]:
        ans = []
        name_counts = {} 

        for name in names:
            current_name = name
            if current_name not in name_counts:
                ans.append(current_name)
                name_counts[current_name] = 1 
            else:
                k = name_counts[current_name]
                new_name = f"{current_name}({k})"
                
                while new_name in name_counts:
                    k += 1
                    new_name = f"{current_name}({k})"
                
                ans.append(new_name)
                
                name_counts[new_name] = 1 
                
                name_counts[current_name] = k + 1 
                
        return ans
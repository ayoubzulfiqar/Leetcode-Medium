class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        
        result = []
        
        for current_folder in folder:
            if not result:
                result.append(current_folder)
            else:
                last_root_folder = result[-1]
                
                is_sub_folder = (
                    current_folder.startswith(last_root_folder) and
                    len(current_folder) > len(last_root_folder) and
                    current_folder[len(last_root_folder)] == '/'
                )
                
                if not is_sub_folder:
                    result.append(current_folder)
                    
        return result
import collections

class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        content_to_paths = collections.defaultdict(list)

        for path_string in paths:
            parts = path_string.split(' ')
            directory_path = parts[0]
            
            for i in range(1, len(parts)):
                file_info = parts[i]
                
                open_paren_idx = file_info.find('(')
                
                file_name = file_info[:open_paren_idx]
                file_content = file_info[open_paren_idx + 1 : -1]
                
                full_file_path = directory_path + "/" + file_name
                
                content_to_paths[file_content].append(full_file_path)
        
        result = []
        for paths_list in content_to_paths.values():
            if len(paths_list) > 1:
                result.append(paths_list)
                
        return result
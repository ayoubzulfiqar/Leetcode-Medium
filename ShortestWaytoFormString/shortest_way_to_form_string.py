class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        count = 0
        target_idx = 0
        t_len = len(target)
        s_len = len(source)

        while target_idx < t_len:
            count += 1
            source_idx = 0
            temp_target_idx = target_idx

            while source_idx < s_len and temp_target_idx < t_len:
                if source[source_idx] == target[temp_target_idx]:
                    temp_target_idx += 1
                source_idx += 1
            
            if temp_target_idx == target_idx:
                return -1
            
            target_idx = temp_target_idx
            
        return count
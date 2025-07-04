class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        required_count = 1 << k
        
        if len(s) < k:
            return False
        
        found_codes = set()
        
        for i in range(len(s) - k + 1):
            substring = s[i : i + k]
            found_codes.add(substring)
            
            if len(found_codes) == required_count:
                return True
                
        return False
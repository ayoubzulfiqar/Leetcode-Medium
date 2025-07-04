def strings_differ_by_one(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    diff_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
            if diff_count > 1:
                return False
    
    return diff_count == 1
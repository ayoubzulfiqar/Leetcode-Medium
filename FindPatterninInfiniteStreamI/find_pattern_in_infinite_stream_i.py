def compute_lps_array(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def find_pattern_in_infinite_stream(stream_iterator, pattern):
    n = len(pattern)
    if n == 0:
        return True

    lps = compute_lps_array(pattern)

    pattern_idx = 0

    try:
        for stream_char in stream_iterator:
            while pattern_idx > 0 and stream_char != pattern[pattern_idx]:
                pattern_idx = lps[pattern_idx - 1]
            
            if stream_char == pattern[pattern_idx]:
                pattern_idx += 1
            
            if pattern_idx == n:
                return True

    except StopIteration:
        return False
    
    return False
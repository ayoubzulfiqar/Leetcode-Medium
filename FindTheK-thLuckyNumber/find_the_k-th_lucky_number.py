import collections

def find_kth_lucky_number(k: int) -> int:
    if k <= 0:
        return -1

    q = collections.deque()
    q.append(4)
    q.append(7)

    count = 0
    while q:
        current_num = q.popleft()
        count += 1

        if count == k:
            return current_num

        next_num_4 = current_num * 10 + 4
        next_num_7 = current_num * 10 + 7
        
        q.append(next_num_4)
        q.append(next_num_7)
    
    return -1
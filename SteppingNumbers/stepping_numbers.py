import collections

class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> list[int]:
        ans = []

        if low == 0:
            ans.append(0)

        q = collections.deque()

        for i in range(1, 10):
            q.append(i)

        while q:
            curr = q.popleft()

            if curr > high:
                continue

            if curr >= low:
                ans.append(curr)

            last_digit = curr % 10

            if last_digit > 0:
                next_num1 = curr * 10 + (last_digit - 1)
                if next_num1 <= high:
                    q.append(next_num1)

            if last_digit < 9:
                next_num2 = curr * 10 + (last_digit + 1)
                if next_num2 <= high:
                    q.append(next_num2)
        
        return ans
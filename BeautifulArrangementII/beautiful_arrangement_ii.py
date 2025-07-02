class Solution:
    def constructArray(self, n: int, k: int) -> list[int]:
        ans = []
        
        # Part 1: Generate k distinct differences (k, k-1, ..., 1)
        # This is achieved by alternating between the smallest available number
        # and the largest available number from the range [1, k+1].
        # This part will construct k+1 elements.
        left = 1
        right = k + 1
        
        for i in range(k + 1):
            if i % 2 == 0:
                ans.append(left)
                left += 1
            else:
                ans.append(right)
                right -= 1
        
        # Part 2: Append the remaining numbers in increasing order.
        # The numbers used in Part 1 are from 1 to k+1.
        # To avoid introducing new distinct differences (other than 1, which is already present),
        # we append numbers from k+2 up to n in sequential order.
        # This ensures that the absolute difference between consecutive elements
        # in this part will always be 1.
        for i in range(k + 2, n + 1):
            ans.append(i)
            
        return ans
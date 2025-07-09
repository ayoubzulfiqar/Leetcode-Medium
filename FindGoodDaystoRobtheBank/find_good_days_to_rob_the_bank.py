class Solution:
    def goodDaysToRobBank(self, security: list[int], time: int) -> list[int]:
        n = len(security)

        if time == 0:
            return list(range(n))

        decr = [0] * n
        for i in range(1, n):
            if security[i-1] >= security[i]:
                decr[i] = decr[i-1] + 1
            else:
                decr[i] = 0
        
        incr = [0] * n
        for i in range(n - 2, -1, -1):
            if security[i] <= security[i+1]:
                incr[i] = incr[i+1] + 1
            else:
                incr[i] = 0
        
        good_days = []
        for i in range(time, n - time):
            if decr[i] >= time and incr[i] >= time:
                good_days.append(i)
        
        return good_days
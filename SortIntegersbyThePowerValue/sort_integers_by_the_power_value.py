class Solution:
    def get_power_value(self, x: int) -> int:
        if x == 1:
            return 0
        if x in self.memo:
            return self.memo[x]

        if x % 2 == 0:
            power = 1 + self.get_power_value(x // 2)
        else:
            power = 1 + self.get_power_value(3 * x + 1)

        self.memo[x] = power
        return power

    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.memo = {} 

        power_values = []
        for num in range(lo, hi + 1):
            power = self.get_power_value(num)
            power_values.append((power, num))

        power_values.sort()

        return power_values[k - 1][1]
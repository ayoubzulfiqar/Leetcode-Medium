class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7

        know = [0] * (n + 1)
        know[1] = 1

        total_aware_count = 1
        current_sharers_count = 0

        for day in range(2, n + 1):
            if day - delay >= 1:
                current_sharers_count = (current_sharers_count + know[day - delay]) % MOD

            if day - forget >= 1:
                current_sharers_count = (current_sharers_count - know[day - forget] + MOD) % MOD
                total_aware_count = (total_aware_count - know[day - forget] + MOD) % MOD

            know[day] = current_sharers_count
            total_aware_count = (total_aware_count + know[day]) % MOD

        return total_aware_count
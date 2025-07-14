import collections

class Solution:
    def max_upgradable_servers(self, n: int, k: int, upgrades: list[int]) -> int:
        upgrade_counts = collections.Counter(upgrades)

        def can_upgrade(num_servers_to_check: int) -> bool:
            if num_servers_to_check == 0:
                return True
            
            total_possible_distinct_slots = 0
            for count in upgrade_counts.values():
                total_possible_distinct_slots += min(count, num_servers_to_check)
            
            return total_possible_distinct_slots >= num_servers_to_check * k

        low = 0
        high = min(n, len(upgrades) // k)
        
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if can_upgrade(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
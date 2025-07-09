class Solution:
    def minimumRemovedBeans(self, beans: list[int]) -> int:
        n = len(beans)
        beans.sort()

        total_sum = sum(beans)
        
        min_removed_beans = total_sum

        for i in range(n):
            num_bags_to_keep_at_current_k = n - i
            beans_remaining_if_target_k = num_bags_to_keep_at_current_k * beans[i]
            current_removed_beans = total_sum - beans_remaining_if_target_k
            
            min_removed_beans = min(min_removed_beans, current_removed_beans)
            
        return min_removed_beans
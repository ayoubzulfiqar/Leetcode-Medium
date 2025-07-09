class Solution:
    def minimalKSum(self, nums: list[int], k: int) -> int:
        sorted_unique_nums = sorted(list(set(nums)))

        appended_sum = 0
        count_appended = 0
        expected_next_num = 1

        for num in sorted_unique_nums:
            if count_appended == k:
                break

            if num > expected_next_num:
                can_append_count = num - expected_next_num

                if count_appended + can_append_count <= k:
                    # Sum of arithmetic series: (count * (first + last)) / 2
                    # first = expected_next_num
                    # last = num - 1
                    appended_sum += (can_append_count * (expected_next_num + num - 1)) // 2
                    count_appended += can_append_count
                else:
                    remaining_needed = k - count_appended
                    # first = expected_next_num
                    # last = expected_next_num + remaining_needed - 1
                    appended_sum += (remaining_needed * (expected_next_num + expected_next_num + remaining_needed - 1)) // 2
                    count_appended = k
                    break
            
            expected_next_num = num + 1

        if count_appended < k:
            remaining_needed = k - count_appended
            # first = expected_next_num
            # last = expected_next_num + remaining_needed - 1
            appended_sum += (remaining_needed * (expected_next_num + expected_next_num + remaining_needed - 1)) // 2
        
        return appended_sum
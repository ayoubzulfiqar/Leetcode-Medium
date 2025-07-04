class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)

        def get_next_idx(current_idx, val, n):
            return (current_idx + val + n) % n

        for i in range(n):
            if nums[i] == 0:
                continue

            slow = i
            fast = i
            
            is_forward = nums[i] > 0

            while True:
                # Move slow pointer one step
                slow = get_next_idx(slow, nums[slow], n)
                if (nums[slow] > 0) != is_forward or nums[slow] == 0:
                    break
                
                # Move fast pointer one step
                fast = get_next_idx(fast, nums[fast], n)
                if (nums[fast] > 0) != is_forward or nums[fast] == 0:
                    break
                
                # Move fast pointer second step
                fast = get_next_idx(fast, nums[fast], n)
                if (nums[fast] > 0) != is_forward or nums[fast] == 0:
                    break
                
                if slow == fast:
                    # Check if the cycle length is greater than 1
                    if get_next_idx(slow, nums[slow], n) != slow:
                        return True
                    else:
                        # This is a self-loop (k=1), not a valid cycle
                        break
            
            # If no valid cycle found from 'i', mark all nodes in this path as visited (0)
            current_path_node = i
            while (nums[current_path_node] > 0) == is_forward and nums[current_path_node] != 0:
                next_node = get_next_idx(current_path_node, nums[current_path_node], n)
                nums[current_path_node] = 0
                current_path_node = next_node
        
        return False
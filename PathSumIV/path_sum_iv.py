class Solution:
    def pathSumIV(self, nums: list[int]) -> int:
        tree_map = {}
        for num in nums:
            depth = num // 100
            position = (num % 100) // 10
            value = num % 10
            tree_map[(depth, position)] = value

        self.total_sum = 0

        def dfs(depth, position, current_path_sum):
            if (depth, position) not in tree_map:
                return

            node_value = tree_map[(depth, position)]
            current_path_sum += node_value

            left_child_key = (depth + 1, 2 * position - 1)
            right_child_key = (depth + 1, 2 * position)

            is_leaf = (left_child_key not in tree_map) and \
                      (right_child_key not in tree_map)

            if is_leaf:
                self.total_sum += current_path_sum
            else:
                dfs(depth + 1, 2 * position - 1, current_path_sum)
                dfs(depth + 1, 2 * position, current_path_sum)

        dfs(1, 1, 0)

        return self.total_sum
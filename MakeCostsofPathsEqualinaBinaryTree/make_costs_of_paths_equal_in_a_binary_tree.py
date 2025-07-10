class Solution:
    def minIncrements(self, n: int, cost: list[int]) -> int:
        total_increments = 0

        # Iterate from the last parent node up to the root (node 1).
        # Node indices are 1-based in the problem description (1 to n).
        # The cost array is 0-indexed (cost[i] corresponds to node i+1).
        # The last parent node in a perfect binary tree is n // 2.
        # We process nodes from bottom-up, starting from the parents of leaves.
        for i in range(n // 2, 0, -1):
            # Convert the 1-based node index 'i' to a 0-based array index.
            current_node_array_idx = i - 1

            # Determine the 1-based indices of the left and right children.
            left_child_node_idx = 2 * i
            right_child_node_idx = 2 * i + 1

            # Retrieve the current maximum path sums from the children to their respective leaves.
            # These values in the 'cost' array have already been updated by previous iterations
            # (for their own subtrees) or are original costs if they are leaf nodes.
            path_sum_from_left_child = cost[left_child_node_idx - 1]
            path_sum_from_right_child = cost[right_child_node_idx - 1]

            # Calculate the number of increments needed to make the path sums from the
            # two children equal. We always increment the smaller path to match the larger one.
            increments_for_children_paths = abs(path_sum_from_left_child - path_sum_from_right_child)
            total_increments += increments_for_children_paths

            # Update the cost of the current node.
            # The new value of cost[current_node_array_idx] will represent the maximum
            # path sum from this node (node i) to any leaf in its subtree,
            # assuming its children's paths are now equalized to the maximum.
            # This updated value will be used by its parent node in the next iteration.
            cost[current_node_array_idx] += max(path_sum_from_left_child, path_sum_from_right_child)
        
        return total_increments
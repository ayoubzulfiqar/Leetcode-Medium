class Solution:
    def depthSumInverse(self, nestedList: ['NestedInteger']) -> int:
        max_depth = self._get_max_depth(nestedList, 1)
        return self._calculate_sum(nestedList, 1, max_depth)

    def _get_max_depth(self, nestedList: ['NestedInteger'], current_depth: int) -> int:
        max_d_in_subtree = current_depth
        for ni in nestedList:
            if not ni.isInteger():
                max_d_in_subtree = max(max_d_in_subtree, self._get_max_depth(ni.getList(), current_depth + 1))
        return max_d_in_subtree

    def _calculate_sum(self, nestedList: ['NestedInteger'], current_depth: int, max_level: int) -> int:
        total_sum = 0
        for ni in nestedList:
            if ni.isInteger():
                weight = max_level - current_depth + 1
                total_sum += ni.getInteger() * weight
            else:
                total_sum += self._calculate_sum(ni.getList(), current_depth + 1, max_level)
        return total_sum
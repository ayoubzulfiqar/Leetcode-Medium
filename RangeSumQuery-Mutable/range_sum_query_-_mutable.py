class NumArray:

    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self._build(0, 0, self.n - 1, nums)

    def _build(self, node: int, start: int, end: int, nums: list[int]):
        if start == end:
            self.tree[node] = nums[start]
        else:
            mid = (start + end) // 2
            self._build(2 * node + 1, start, mid, nums)
            self._build(2 * node + 2, mid + 1, end, nums)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, index: int, val: int) -> None:
        self._update_tree(0, 0, self.n - 1, index, val)

    def _update_tree(self, node: int, start: int, end: int, index: int, val: int):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if start <= index <= mid:
                self._update_tree(2 * node + 1, start, mid, index, val)
            else:
                self._update_tree(2 * node + 2, mid + 1, end, index, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def sumRange(self, left: int, right: int) -> int:
        return self._query_tree(0, 0, self.n - 1, left, right)

    def _query_tree(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        p1 = self._query_tree(2 * node + 1, start, mid, left, right)
        p2 = self._query_tree(2 * node + 2, mid + 1, end, left, right)
        return p1 + p2
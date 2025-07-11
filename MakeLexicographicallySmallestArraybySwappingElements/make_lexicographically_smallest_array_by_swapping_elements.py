import collections

class Solution:
    def makeLexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)
        parent = list(range(n))
        size = [1] * n

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                if size[root_i] < size[root_j]:
                    root_i, root_j = root_j, root_i
                parent[root_j] = root_i
                size[root_i] += size[root_j]
                return True
            return False

        indexed_nums = [(nums[i], i) for i in range(n)]
        indexed_nums.sort()

        for i in range(n - 1):
            val1, idx1 = indexed_nums[i]
            val2, idx2 = indexed_nums[i+1]
            if val2 - val1 <= limit:
                union(idx1, idx2)

        components = collections.defaultdict(lambda: {'indices': [], 'values': []})
        for i in range(n):
            root = find(i)
            components[root]['indices'].append(i)
            components[root]['values'].append(nums[i])

        ans = [0] * n
        for root in components:
            indices_in_component = sorted(components[root]['indices'])
            values_in_component = sorted(components[root]['values'])

            for k in range(len(indices_in_component)):
                ans[indices_in_component[k]] = values_in_component[k]
        
        return ans
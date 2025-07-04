import collections

class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        groups_by_size = collections.defaultdict(list)
        
        n = len(groupSizes)
        for i in range(n):
            size = groupSizes[i]
            groups_by_size[size].append(i)
            
        final_groups = []
        
        for size, people_ids in groups_by_size.items():
            for i in range(0, len(people_ids), size):
                current_group = people_ids[i : i + size]
                final_groups.append(current_group)
                
        return final_groups
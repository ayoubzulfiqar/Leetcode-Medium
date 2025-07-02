import collections

class Solution:
    def loudAndRich(self, richer: list[list[int]], quiet: list[int]) -> list[int]:
        n = len(quiet)
        
        adj_rev = collections.defaultdict(list)
        for a, b in richer:
            adj_rev[b].append(a)
        
        answer = [-1] * n
        
        def dfs(person_id: int) -> int:
            if answer[person_id] != -1:
                return answer[person_id]
            
            min_quiet_person = person_id
            
            for richer_person in adj_rev[person_id]:
                candidate_person = dfs(richer_person)
                
                if quiet[candidate_person] < quiet[min_quiet_person]:
                    min_quiet_person = candidate_person
            
            answer[person_id] = min_quiet_person
            return min_quiet_person

        for i in range(n):
            dfs(i)
            
        return answer
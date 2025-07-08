from collections import defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: list[list[int]], k: int) -> list[int]:
        user_activity = defaultdict(set)

        for user_id, time in logs:
            user_activity[user_id].add(time)

        answer = [0] * k

        for uam_set in user_activity.values():
            uam = len(uam_set)
            if 1 <= uam <= k:
                answer[uam - 1] += 1
        
        return answer
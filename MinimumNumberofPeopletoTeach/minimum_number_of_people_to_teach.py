class Solution:
    def minimumTeachings(self, n: int, languages: list[list[int]], friendships: list[list[int]]) -> int:
        num_users = len(languages)

        user_languages = [set(langs) for langs in languages]

        uncommunicable_friends = []
        for u, v in friendships:
            u_idx = u - 1
            v_idx = v - 1

            if not (user_languages[u_idx] & user_languages[v_idx]):
                uncommunicable_friends.append((u_idx, v_idx))
        
        if not uncommunicable_friends:
            return 0

        min_teach_count = float('inf')

        for lang_to_teach in range(1, n + 1):
            users_to_teach_this_lang = set()
            
            for u_idx, v_idx in uncommunicable_friends:
                if lang_to_teach not in user_languages[u_idx]:
                    users_to_teach_this_lang.add(u_idx)
                if lang_to_teach not in user_languages[v_idx]:
                    users_to_teach_this_lang.add(v_idx)
            
            min_teach_count = min(min_teach_count, len(users_to_teach_this_lang))
        
        return min_teach_count
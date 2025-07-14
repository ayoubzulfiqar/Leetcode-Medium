class Solution:
    def isSpam(self, message: list[str], bannedWords: list[str]) -> bool:
        banned_set = set(bannedWords)
        spam_count = 0
        for word in message:
            if word in banned_set:
                spam_count += 1
                if spam_count >= 2:
                    return True
        return False
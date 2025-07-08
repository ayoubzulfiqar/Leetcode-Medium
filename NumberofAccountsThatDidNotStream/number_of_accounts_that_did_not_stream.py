class Solution:
    def numberOfAccountsThatDidNotStream(self, accounts: list[list[int, bool]]) -> int:
        count = 0
        for account in accounts:
            # Assuming each inner list is [account_id, has_streamed_status]
            # where has_streamed_status is a boolean (True if streamed, False otherwise)
            if not account[1]:
                count += 1
        return count
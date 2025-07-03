class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        letter_logs = []
        digit_logs = []

        for log in logs:
            # Check the second word (first word after identifier) to determine log type
            # If it's a digit, it's a digit-log; otherwise, it's a letter-log.
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # Sort letter-logs based on the specified criteria
        # The sorting key is a tuple: (content_part, identifier_part)
        # content_part: everything after the first space (the identifier)
        # identifier_part: the first word of the log
        letter_logs.sort(key=lambda log: (log.split(' ', 1)[1], log.split(' ', 1)[0]))

        # Combine the sorted letter-logs with the digit-logs (which maintain their original relative order)
        return letter_logs + digit_logs
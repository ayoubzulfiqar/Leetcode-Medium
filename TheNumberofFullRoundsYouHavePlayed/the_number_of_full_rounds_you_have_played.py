class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        
        def time_to_minutes(time_str: str) -> int:
            h = int(time_str[:2])
            m = int(time_str[3:])
            return h * 60 + m

        login_minutes = time_to_minutes(loginTime)
        logout_minutes = time_to_minutes(logoutTime)

        if logout_minutes < login_minutes:
            logout_minutes += 24 * 60

        first_valid_round_start = (login_minutes + 14) // 15 * 15
        last_valid_round_start = (logout_minutes - 15) // 15 * 15

        if first_valid_round_start > last_valid_round_start:
            return 0
        
        return (last_valid_round_start - first_valid_round_start) // 15 + 1
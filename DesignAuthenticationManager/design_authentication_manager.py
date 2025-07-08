class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {} # Stores tokenId -> expiration_time

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        # Check if the token exists and is unexpired at the current time.
        # A token is considered unexpired if its expiration time is strictly greater than currentTime.
        # If a token expires at time t, and an action happens at time t, the expiration takes place before the action.
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive
        # If the token does not exist or is already expired, the request is ignored.

    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        # Iterate through all stored tokens and count those that are unexpired.
        # A token is unexpired if its expiration time is strictly greater than currentTime.
        for exp_time in self.tokens.values():
            if exp_time > currentTime:
                count += 1
        return count
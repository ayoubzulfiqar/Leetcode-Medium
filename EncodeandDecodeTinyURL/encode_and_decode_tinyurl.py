class Solution:
    def __init__(self):
        self.long_to_short = {}
        self.short_to_long = {}
        self.base_url = "http://tinyurl.com/"
        self.counter = 0

    def encode(self, longUrl: str) -> str:
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]

        self.counter += 1
        short_id = str(self.counter)
        shortUrl = self.base_url + short_id

        self.long_to_short[longUrl] = shortUrl
        self.short_to_long[shortUrl] = longUrl

        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.short_to_long[shortUrl]
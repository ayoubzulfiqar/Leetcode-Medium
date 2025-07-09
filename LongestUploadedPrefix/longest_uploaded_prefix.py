class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.uploaded_videos = [False] * (n + 1)
        self.longest_prefix_len = 0

    def upload(self, video: int) -> None:
        self.uploaded_videos[video] = True
        while self.longest_prefix_len + 1 <= self.n and self.uploaded_videos[self.longest_prefix_len + 1]:
            self.longest_prefix_len += 1

    def longest(self) -> int:
        return self.longest_prefix_len
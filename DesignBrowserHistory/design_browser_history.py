class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_idx = 0
        self.max_idx = 0

    def visit(self, url: str) -> None:
        self.current_idx += 1
        if self.current_idx < len(self.history):
            self.history[self.current_idx] = url
        else:
            self.history.append(url)
        self.max_idx = self.current_idx

    def back(self, steps: int) -> str:
        self.current_idx = max(0, self.current_idx - steps)
        return self.history[self.current_idx]

    def forward(self, steps: int) -> str:
        self.current_idx = min(self.max_idx, self.current_idx + steps)
        return self.history[self.current_idx]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
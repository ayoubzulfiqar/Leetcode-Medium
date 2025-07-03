class StockSpanner:

    def __init__(self):
        self.stack = [] # Stores (price, span) pairs

    def next(self, price: int) -> int:
        current_span = 1
        
        # While the stack is not empty and the price at the top of the stack
        # is less than or equal to the current price, pop elements
        # and add their spans to the current_span.
        while self.stack and self.stack[-1][0] <= price:
            current_span += self.stack.pop()[1]
            
        # Push the current price and its calculated span onto the stack
        self.stack.append((price, current_span))
        
        return current_span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        span = 1
        while self.st and self.st[-1][0] <= price:
            old_price, old_span = self.st.pop()
            span += old_span
        self.st.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
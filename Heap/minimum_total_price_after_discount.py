from heapq import *


class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        h = []
        heapify(h)

        final_prices = []

        for price in prices:
            heappush(h, -price)

        discounts = sorted(discounts, reverse=True)

        for i in range(len(discounts)):
            if h:
                final_prices.append((-h[0] * (100 - discounts[i])) / 100)
                heappop(h)

        while h:
            final_prices.append(-h[0])
            heappop(h)

        return sum(final_prices)
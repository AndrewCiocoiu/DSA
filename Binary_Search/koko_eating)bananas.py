class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def validate(eating_speed):
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / eating_speed)
            return hours <= h
        
        low = 1
        high = max(piles)

        while low < high:
            mid = (low + high) // 2

            if validate(mid):
                high = mid
            else:
                low = mid + 1

        return low
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        res = []

        for kid in candies:
            if kid + extraCandies >= max_candies:
                res.append(True)
            else:
                res.append(False)

        return res
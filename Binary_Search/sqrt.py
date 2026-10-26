class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x + 1
        while left < right:
            mid = (left + right) // 2   

            res = mid * mid

            if res == x:
                return mid
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1
        
        return left - 1
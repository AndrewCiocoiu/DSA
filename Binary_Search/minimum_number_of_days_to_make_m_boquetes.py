class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        def validate(day):
            current_bloomed = 0
            total_boquetes = 0

            for bloom in bloomDay:
                if bloom <= day:
                    current_bloomed += 1
                    if current_bloomed == k:
                        total_boquetes += 1
                        current_bloomed = 0
                else:
                    current_bloomed = 0
            
            return m <= total_boquetes

        left = 1
        right = max(bloomDay) + 1

        while left < right:
            mid = (left + right) // 2

            if(validate(mid)):
                right = mid
            else:
                left = mid + 1
        
        return left if validate(left) else -1




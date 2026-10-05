class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def validate(max_weight):
            i = 0
            current_days = days
            while i != len(weights):
                current_weight = max_weight
                while(weights[i] <= current_weight):
                    current_weight -= weights[i]
                    i += 1
                    if i == len(weights):
                        return True
                current_days -= 1
                if current_days == 0:
                    return False
            return True
        
        low = 1
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2

            if(validate(mid)):
                high = mid
            else:
                low = mid + 1
        
        return low
                


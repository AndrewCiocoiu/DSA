class Solution:
    cache = {}
    
    def tribonacci(self, n: int) -> int:
        if n == 2:
            return 1
        if n < 2:
            return n
        if n in self.cache:
            return self.cache[n]
        
        n_sum = self.tribonacci(n -1) + self.tribonacci(n - 2) + self.tribonacci(n - 3) 

        self.cache[n] = n_sum

        return n_sum
        
class Solution:
    def numDecodings(self, s: str) -> int:
        dp  = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0

        for i in range(2, len(s) + 1):
            one = int(s[i - 1])
            two = int(s[i - 2:i])

            if one >= 1 and one <= 9:
                dp[i] += dp[i - 1]
            if two >=10 and two <= 26:
                dp[i] += dp[i - 2]
        
        return dp[len(s)]

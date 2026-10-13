class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        st = []
        res = [0] * len(prices)

        for i in range(len(prices) - 1, -1, -1):
            while st and st[-1] > prices[i]:
                st.pop()
            
            if st:
                res[i] = prices[i] - st[-1]
            else:
                res[i] = prices[i]
            
            st.append(prices[i])

        return res
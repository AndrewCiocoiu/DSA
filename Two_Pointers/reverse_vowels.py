class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        left = 0
        right = len(s) - 1

        s_list = list(s)

        while left < right:
            if s_list[left] in vowels:
                if s_list[right] in vowels:
                    s_list[left], s_list[right] = s_list[right], s_list[left]
                    right -= 1
                    left += 1
                elif s_list[right] not in vowels:
                    right -= 1
            else:
                left += 1
        
        return "".join(s_list)
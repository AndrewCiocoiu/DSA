class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiouAEIOU")

        left = 0
        right = k

        count = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        maxCount = count

        for right in range(k, len(s)):
            if s[right] in vowels:
                count += 1
            if s[left] in vowels:
                count -= 1

            maxCount = max(maxCount, count)

            left += 1

        return maxCount
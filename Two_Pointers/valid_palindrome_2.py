class Solution:
    def validPalindrome(self, s: str) -> bool:
        k = 1
        right = len(s) - 1
        left = 0

        while left < right:
            if s[left] != s[right]:
                skip_left = s[left + 1 : right + 1]
                skip_right = s[left : right]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            else:
                left += 1
                right -= 1
        
        return True
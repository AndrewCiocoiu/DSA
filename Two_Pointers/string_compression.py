class Solution:
    def compress(self, chars: List[str]) -> int:
        
        left = 0
        count = 0
        curr = chars[0]
        
        for right in range(len(chars)):
            if chars[right] != curr:
                if count == 1:
                    chars[left] = curr
                    left += 1
                else:
                    chars[left] = curr
                    left += 1
                    if count > 9:
                        for digit in str(count):
                            chars[left] = str(digit)
                            left += 1
                    else:
                        chars[left] = str(count)
                        left += 1
                curr = chars[right]
                count = 1
            else:
                count += 1
        
        if count == 1:
            chars[left] = curr
            left += 1
        else:
            chars[left] = curr
            left += 1
            if count > 9:
                for digit in str(count):
                    chars[left] = str(digit)
                    left += 1
            else:
                chars[left] = str(count)
                left += 1
        
        for i in range(right - left + 1):
            chars.pop()
        
        return len(chars)
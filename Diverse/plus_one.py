class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_num = int("".join([str(x) for x in digits])) + 1

        res = [int(x) for x in str(new_num)]
        return res
        
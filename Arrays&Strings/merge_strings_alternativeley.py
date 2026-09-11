class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_word = ""
        for l1, l2 in zip(word1, word2):
            final_word += l1 + l2
        
        if len(word1) > len(word2):
            final_word += word1[len(word2):]
        elif len(word1) < len(word2):
            final_word += word2[len(word1):]

        return final_word

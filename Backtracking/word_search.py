class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def backtrack(r, c, k):
            if k == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or word[k] != board[r][c]:
                return False
            
            temp = board[r][c]
            board[r][c] = "#"

            found = (
                backtrack(r + 1, c, k + 1) or
                backtrack(r - 1, c, k + 1) or
                backtrack(r, c + 1, k + 1) or
                backtrack(r, c - 1, k + 1)
            )

            board[r][c] = temp

            return found
        
        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False
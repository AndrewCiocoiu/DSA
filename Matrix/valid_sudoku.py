class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seen = set()
            for j in range(len(board[0])):
                if board[i][j].isdigit():
                    num = board[i][j]
                else:
                    continue

                if num in seen:
                    return False

                seen.add(num)

        for j in range(len(board)):
            seen = set()
            for i in range(len(board[0])):
                if board[i][j].isdigit():
                    num = board[i][j]
                else:
                    continue

                if num in seen:
                    return False

                seen.add(num)

        for r in range(3):
            for c in range(3):
                seen = set()
                for i in range(3 * r, 3 * (r + 1)):
                    for j in range(3 * c, 3 * (c + 1)):
                        if board[i][j].isdigit():
                            num = board[i][j]
                        else:
                            continue

                        if num in seen:
                            return False

                        seen.add(num)

        return True

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.sum_mat = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        self.matrix_data = matrix

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.sum_mat[r][c + 1]
                self.sum_mat[r + 1][c + 1] = prefix + above

    def print_matrix(self):
        if not self.matrix_data:
            return

        rows = len(self.matrix_data)
        cols = len(self.matrix_data[0])

        for row in range(rows):
            for col in range(cols):
                print(self.matrix_data[row][col], end = " ")
            print()

        print()

    def print_sum_matrix(self):
        if not self.sum_mat:
            return

        rows = len(self.sum_mat)
        cols = len(self.sum_mat[0])

        for row in range(1, rows):
            for col in range(1, cols):
                print(self.sum_mat[row][col], end = " ")
            print()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottom_right = self.sum_mat[r2][c2]
        above = self.sum_mat[r1 - 1][c2]
        left = self.sum_mat[r2][c1 - 1]
        top_left = self.sum_mat[r1 - 1][c1 - 1]

        return bottom_right - above - left + top_left

matrix = [
    [3, 0, 1, 4, 2], 
    [5, 6, 3, 2, 1], 
    [1, 2, 0, 1, 5], 
    [4, 1, 0, 1, 7], 
    [1, 0, 3, 0, 5]
    ]

m = NumMatrix(matrix)
m.print_matrix()
m.print_sum_matrix()




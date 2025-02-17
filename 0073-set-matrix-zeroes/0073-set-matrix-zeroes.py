class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        row = [0] * n  # row array
        col = [0] * m  # col array

        # Traverse the matrix:
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    # mark ith index of row wih 1:
                    row[i] = 1

                    # mark jth index of col wih 1:
                    col[j] = 1

        # Finally, mark all (i, j) as 0
        # if row[i] or col[j] is marked with 1.
        for i in range(n):
            for j in range(m):
                if row[i] or col[j]:
                    matrix[i][j] = 0

        return matrix




    # def markRow(self, matrix: List[List[int]], i: int):
    #     for j in range(len(matrix[0])):
    #         if matrix[i][j] != 0:
    #             matrix[i][j] = -1

    # def markCol(self, matrix: List[List[int]], j: int):
    #     for i in range(len(matrix)):
    #         if matrix[i][j] != 0:
    #             matrix[i][j] = -1

    # def setZeroes(self, matrix: List[List[int]]) -> None:
    #     """
    #     Do not return anything, modify matrix in-place instead.
    #     """
    #     rows = len(matrix)
    #     cols = len(matrix[0])

    #     for i in range(rows):
    #         for j in range(cols):
    #             if matrix[i][j] == 0:
    #                 self.markRow(matrix, i)
    #                 self.markCol(matrix, j)
                
    #     for i in range(rows):
    #         for j in range(cols):
    #             if matrix[i][j] == -1:
    #                 matrix[i][j] = 0
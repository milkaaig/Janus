class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        c = len(matrix[0])
        r = len(matrix)
        j = 0

        for i in range(r):
            for j in range(c):
                if i + 1 < r and j + 1  < c:
                    if matrix[i][j] != matrix[i + 1][j + 1]:
                        return False

        return True

            
        
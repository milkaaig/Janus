class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        done = []

        def zero(r,c):
           
            for i in range(row):
                matrix[i][c] = 0
            
            for j in range(col):
                matrix[r][j] = 0


        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    done.append([i,j])
        
        for point in done:
            r,c = point
            zero(r,c)
        
     
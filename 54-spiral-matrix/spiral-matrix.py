class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        output = []
        
      

        
        left,top = 0,0
        right, bottom = col - 1, row-1
        # -1 offset helps in indexing the correct matrix element when traversing

        while left <= right and top <= bottom:
            # left to right - Top row
            for i in range(left, right + 1):
                output.append(matrix[top][i])            
            top += 1
            
            # top to bottom - right col
            for i in range(top,bottom + 1):
                output.append(matrix[i][right])
            right -= 1
            
            #right to left - bottom row
            if bottom >= top:
                #on the last iteration since top and right will be incremented above we need to   include it for both 
                for i in range(right,left - 1,-1):
                    output.append(matrix[bottom][i])
                bottom -= 1
            
            
            # bottom to top - left col
            if right >= left:
                for i in range(bottom,top - 1, -1):

                    output.append(matrix[i][left])
                left += 1
        

        

        return output




                    
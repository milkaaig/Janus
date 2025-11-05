class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mc = len(mat[0])
        mr = len(mat)

        if  r*c != mc*mr:
            return mat
        
        matList = []

        for i in range(mr):
            for j in range(mc):
                matList.append(mat[i][j])

        output = []
        for row in range(r):
            output.append(matList[row * c: (row * c) + c])
        

        return output

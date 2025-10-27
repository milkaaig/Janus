from collections import defaultdict
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    
        n = len(arr)
        if n == 1:
            return [-1]
        if n == 2:
            return [arr[1],-1]

        
        greatest = max(arr[-1], arr[-2])
        for i in range(n-3, -1, -1):

            curr = arr[i]
            arr[i] = greatest
            greatest = max(greatest, curr) 

       
        

        arr[-2] = arr[-1]
        arr[-1] = -1

        return arr 

        
        
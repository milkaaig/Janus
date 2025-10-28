class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        m = -1
        before = -1

        if max(arr) == arr[0] or max(arr) == arr[n-1]:
            return False

        if n < 3:
            return False

        for  i in range(n):
            if before == arr[i]:
                return False

            if m == -1 :
                if arr[i] > before:
                    before = arr[i]
                else:
                    m = before
                    before = arr[i]
            else:
                if arr[i] > before:
                    return False
                before = arr[i]
        
        return m != -1
                
                
                
        
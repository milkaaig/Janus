class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        col = len(strs[0])

        i = 0
        deleteCol = 0
        checked = set()

        while i < (n - 1):
            for c in range (col):
                if c not in checked:
                    if strs[i][c]  > strs[i + 1][c]:
                        checked.add(c)
                        deleteCol += 1 

            i += 1

        return deleteCol
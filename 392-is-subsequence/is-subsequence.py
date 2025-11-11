class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ns = len(s)
        nt = len(t)

        i = 0
        if not s:
            return True
        
        for j in range(nt):
            if t[j] == s[i]:
                if i == ns - 1:
                    return  True
                i += 1
        
        return False
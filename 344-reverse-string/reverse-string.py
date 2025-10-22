class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        originalOrder = dict()
        n = len(s)

        for i in range(n):
            originalOrder[i] = s[i]

        for i in range(n):
            s[i] = originalOrder[n-(i + 1)]
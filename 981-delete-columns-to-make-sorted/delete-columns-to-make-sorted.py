class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0

        # Transposing the characters into columns
        for col in zip(*strs):
            if list(col) != sorted(list(col)):
                result += 1

        return result
from collections import defaultdict

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        output = []

        ref = defaultdict(int)
        for char in words[0]:
            ref[char] += 1

        for i in range(1, n):
            for char in words[0]:
                if char not in words[i]:
                    ref[char] = 0
                else:
                    ref[char] = min(ref[char], words[i].count(char))
        for key, val in ref.items():
            if val > 0:
                output.extend(key * val)

        return output


      
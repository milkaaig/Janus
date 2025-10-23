from collections import defaultdict

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        output = []
        single = defaultdict(int)
       
        for char in words[0]:
            single[char] += 1

        for char, freq in single.items():
            minm = 101
            for i in range(n):
                x = words[i].count(char)
               
                minm = min(minm, x)

            if minm > 0:
                output.extend(char * minm)
      
        return output
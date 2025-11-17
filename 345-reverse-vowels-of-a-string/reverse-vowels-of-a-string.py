class Solution:
    def reverseVowels(self, s: str) -> str:
        n = len(s)
        l = 0
        r = n-1
        vowels = {'a','A','e','E','i','I','o','O','u','U'}

        while l < r:
            if s[l] in vowels and s[r] in vowels:
                s = s[:l] + s[r] + s[l + 1:r] + s[l] + s[r +1:]
                l += 1
                r -= 1
            elif s[r] not in vowels:
                r -= 1
            elif s[l] not in vowels :
                l += 1

        
        return s
        
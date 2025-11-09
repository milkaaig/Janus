class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ''
        n1 = len(word1)
        n2 = len(word2)
        
        first = min(n1,n2)
        

        for i in range(first):
            output += word1[i]
            output += word2[i]

        if n1 > n2:
            output = ''.join([output, word1[first: ]])
        elif n2 > n1:
            output = ''.join([output, word2[first:]])

        return  output
        


        

        return output


        
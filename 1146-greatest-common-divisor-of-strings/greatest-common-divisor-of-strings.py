class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        
        if str1 + str2 != str2 + str1:
            return ""
        
        
        

        if str1 == str2:
            return str1

        n1 = len(str1)
        n2 = len(str2)
       
        
        big= max(n1,n2)
        small = min(n1,n2)
        mod = small
        quot = 0

        while mod > 0:
            mod = big % small
            big = small
            small = mod



        return str1[:big]
            
            

        
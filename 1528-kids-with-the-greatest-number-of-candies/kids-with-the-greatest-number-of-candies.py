class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        n = len(candies)
        output = [False] * n

        for i in range(n):
            if candies[i] + extraCandies >= greatest:
                output[i] = True
        
        return output
        
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct = set(nums)
        n = len(nums)

        for num in nums:
            s = str(num)
            
            distinct.add(int(s[::-1]))
        
        return len(distinct)
        
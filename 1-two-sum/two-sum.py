from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        check = defaultdict(int)
        c = set(nums)
        n = len(nums)
        second = 0

        for num in nums:
            check[num] += 1

      
        for i in range(n):
            d = target - nums[i]
            if d in c:
                if d == nums[i] and check[d] == 1:
                    continue
                output.append(i)
                


        
        return output
        
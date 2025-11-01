from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = []
        check = defaultdict(int)
        n = len(nums)

      
        for i in range(n):
            if nums[i] in check and (nums[i] + nums[check[nums[i]]]) == target:
                output.append(i)
                output.append(check[nums[i]])
                return output
            
            check[target - nums[i]] = i


        
        
        
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        n = len(nums)
        below = 0
        are = 0

        for i in range(n):
            if nums[i] == target:
                are += 1
            elif nums[i] < target:
                below += 1
        
        for j in range(are):
            output.append((below) + j)


        return output
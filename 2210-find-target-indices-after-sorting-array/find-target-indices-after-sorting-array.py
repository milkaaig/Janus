class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        output = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if nums[i] == target:
                output.append(i)


        return output
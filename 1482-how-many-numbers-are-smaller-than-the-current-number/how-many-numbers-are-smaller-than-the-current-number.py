class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        store = dict()

        sortedNums = sorted(nums, reverse = True)
        for i in range(n):
            store[sortedNums[i]] = (n -1) - i
        
        output = []

        for i in range(n):
            output.append(store[nums[i]])

        return output
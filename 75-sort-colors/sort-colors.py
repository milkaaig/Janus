class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = {0: 0, 1: 0, 2: 0}
        

        for n in nums:
            counter[n] += 1
        
        zerofreq = counter[0]
        onefreq = counter[1]
        twofreq = counter[2]

        track = 0
        n = len(nums)
        for i in range(track,zerofreq):
            nums[i] = 0

        track += zerofreq

        for j in range(track, (track + onefreq)):
            nums[j]  = 1 
        
        track += onefreq

        for k in range(track, (track + twofreq)):
            nums[k] = 2
                    
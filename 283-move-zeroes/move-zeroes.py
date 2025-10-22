class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        p= 0

        for i in range(n):
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1
                
        for i in range(p, n):

            nums[i] = 0


            

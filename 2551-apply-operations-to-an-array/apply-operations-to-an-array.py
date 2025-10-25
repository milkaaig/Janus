class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        i = 0

        while i < (n-1) :
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
            i += 1

        left = 0
        right = 1
        while right < n:
            if nums[left] > 0:
                right += 1
                left += 1
            
            elif  nums[left] == 0:
                if nums[right] > 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right += 1
                else:
                    right += 1

        return nums


        
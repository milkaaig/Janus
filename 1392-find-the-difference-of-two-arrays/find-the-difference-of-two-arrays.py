class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        notIn1 = []
        notIn2 = []

        for i in set1:
            if i not in set2:
                notIn2.append(i)
        for i in set2:
            if i  not in set1:
                notIn1.append(i)
        output = []
        output.append(notIn2)
        output.append(notIn1)

        return output
        
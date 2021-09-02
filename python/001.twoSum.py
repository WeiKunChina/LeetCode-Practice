class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, element in enumerate(nums):
            if target - element in d:
                return [d[target - element], i]
            d[element] = i

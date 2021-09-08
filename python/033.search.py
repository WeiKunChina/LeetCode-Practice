class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            if nums[middle] >= nums[start]:
                if nums[start] <= target < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if nums[middle] <= target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
        return -1

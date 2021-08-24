class Solution(object):
    """
    整体思路：首先数组是一个有序数组的旋转，从这个条件可以看出，数组是有大小规律的，可以使用二分查整体思路：首先数组是一个有序数组的旋转，从这个条件可以看出，数组是有大小规律的，可以使用二分查
    时间复杂度：O(logn)，空间复杂度：O(1)
    """
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = nums[0]
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) / 2
            if nums[start] < nums[mid]:
                start = mid
            elif nums[start] > nums[mid]:
                end = mid
            else:
                start += 1
                answer = min(answer, nums[start])
        return min(answer, nums[start], nums[end])

    def findMinOptimize(self, numbers):
        """
        :param numbers: List[int]
        :return: int
        """
        start, end = 0, len(numbers) - 1
        while start < end:
            mid = start + (end - start) / 2
            if numbers[mid] < numbers[end]:
                end = mid
            elif numbers[mid] > numbers[end]:
                start = mid + 1
            else:
                end -= 1
        return numbers[start]
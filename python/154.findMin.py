# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变
# 化后可能得到：
#  若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
#  若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
#
#  注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2],
# ..., a[n-2]] 。
#
#  给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

#  示例 1：
# 输入：nums = [1,3,5]
# 输出：1
#
#  示例 2：
# 输入：nums = [2,2,2,0,1]
# 输出：0
#
#  提示：
#  n == nums.length
#  1 <= n <= 5000
#  -5000 <= nums[i] <= 5000
#  nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
#
#  进阶：
#  这道题是 寻找旋转排序数组中的最小值 的延伸题目。
#  允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

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
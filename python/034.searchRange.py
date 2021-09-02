# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#  如果数组中不存在目标值 target，返回 [-1, -1]。
#  进阶：
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

#  示例 1：
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
#  示例 2：
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
#
#  示例 3：
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#  提示：
#  0 <= nums.length <= 10⁵
#  -10⁹ <= nums[i] <= 10⁹
#  nums 是一个非递减数组
#  -10⁹ <= target <= 10⁹
class Solution(object):
    def searchRangeCompulsive(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target not in nums:
            return [-1, -1]
        if len(nums) == 1 and target in nums:
            return [0, 0]
        elif len(nums) == 1 and target not in nums:
            return [-1, -1]
        else:
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] != target:
                    left += 1
                if nums[right] != target:
                    right -= 1
                if nums[left] == nums[right] == target:
                    return [left, right]

    def searchRangeBinary(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = []
        if not nums:
            return [-1, -1]
        if len(nums) == 1 and target == nums[0]:
            return [0, 0]
        elif len(nums) == 1 and target != nums[0]:
            return [-1, -1]
        else:
            # 检测左边界
            left, right = 0, len(nums) - 1
            while left < right:
                middle = left + (right - left) // 2
                if nums[middle] >= target:
                    right = middle
                else:
                    left = middle + 1
            # 不存在直接返回
            if nums[left] != target:
                return [-1, -1]
            result.append(left)

            # 检测右边界
            if left == len(nums) - 1:
                result.append(left)
                return result
            elif nums[left] != nums[left + 1]:
                result.append(left)
                return result
            else:
                right = len(nums) - 1
                while left < right:
                    middle = (right + left + 1) // 2
                    if nums[middle] <= target:
                        left = middle
                    elif nums[middle] > target:
                        right = middle - 1
                result.append(right)
            return result

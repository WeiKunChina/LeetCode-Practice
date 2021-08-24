class Solution(object):
    def searchMatrixCondition(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[-1]:
            return False
        x, y = 0, len(matrix) - 1
        while x < len(matrix[-1]) and 0 <= y:
            if matrix[y][x] < target:
                x += 1
            elif matrix[y][x] > target:
                y -= 1
            else:
                return True
        return False

    def searchMatrixBinary(self, matrix, target):
        """
        利用二分查找加速
        :param matrix: List[List[int]]
        :param target: int
        :return: bool
        """
        def binarySearch(nums, target):
            start, end = 0, len(nums) - 1
            if nums[start] == target:
                return True
            if nums[end] == target:
                return True
            while start + 1 < end:
                mid = start + (end - start) / 2
                if nums[mid] > target:
                    end = mid
                elif nums[mid] < target:
                    start = mid
                else:
                    return True
            return False

        for nums in matrix:
            if binarySearch(nums, target):
                return True
        return False

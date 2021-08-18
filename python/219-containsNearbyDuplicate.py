class Solution(object):
    def containsNearbyDuplicateDict(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        if k == 0:
            return False
        # 问题解答，遍历数组存储到dict中，key为数组的值，value为索引值
        result = dict()
        for index, value in enumerate(nums):
            if value not in result:
                # 不存在就存下来
                result[value] = index 
            elif abs(result[value] - index) <= k:
                # 如果存在重复且距离在k以内，返回
                return True
            else:
                # 如果距离不满足，更新标记
                result[value] = index
        return False

    
    def containsNearbyDuplicateSet(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return False
        if k == 0:
            return False
        tmp = set()
        for i in range(len(nums)):
            if nums[i] in tmp:
                return True
            # 将第i个元素放到set中
            tmp.add(nums[i])
            if len(tmp) > k:
                # 将第i-k个元素移除
                tmp.remove(nums[i - k])
        return False
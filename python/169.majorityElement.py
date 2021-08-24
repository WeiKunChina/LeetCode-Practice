import collections
class Solution(object):
    """
    本题常见解法共有 3 种
        1.数组排序：首先将 nums 排序，由于该数字超过数组长度的一半，所以数组的中间元素就是答案，时间复杂度为 O(nlogn)
        2.哈希计数：遍历 nums 数组，将数字存在 HashMap 中，统计数字出现次数，统计完成后再遍历一次 HashMap，找到超过一半计数的数字，时间复杂度为 O(n)
        3.摩尔投票：遍历 nums 数组，使用 count 进行计数，记录当前出现的数字为 cur，如果遍历到的 num 与 cur 相等，则 count 自增，否则自减，当其减为 0 时则将 cur 修改为当前遍历的 num，通过增减抵消的方式，最终达到剩下的数字是结果的效果，时间复杂度为 O(n)
    """
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[int(len(nums) / 2)]

    def majorityElement2(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement3(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

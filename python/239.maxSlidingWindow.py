import collections


class Solution(object):
    def maxSlidingWindowViolence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        if k == 0:
            return result
        left, right = 0, k
        while right < len(nums) + 1:
            result.append(max(nums[left: right]))
            left += 1
            right += 1
        return result

    def maxSlidingWindow(self, nums, k):
        """
        1.使用一个队列存储所有还没有被移除的下标。在队列中，这些下标按照从小到大的顺序被存储，并且它们在数组 nums 中对应的值是严格单调递减的。
        2.当滑动窗口向右移动时，我们需要把一个新的元素放入队列中。为了保持队列的性质，我们会不断地将新的元素与队尾的元素相比较，如果前者大于等于后者，那么队尾的元素就可以被永久地移除，我们将其弹出队列。我们需要不断地进行此项操作，直到队列为空或者新的元素小于队尾的元素。
        时间复杂度O(n),空间复杂度O(k)
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if k == 0:
            return []
        result = []
        stack = collections.deque([])
        # 第一个窗口，存储窗口中从大到小的值的索引
        for i in range(k):
            while stack and nums[stack[-1]] < nums[i]:
                # 窗口内，在该值的后面有比这个值大的值存在，所以该值没有存在的必要，这样可以保障有序，而且左边的值是窗口内最大的元素的索引~
                stack.pop()
            stack.append(i)
        result.append(nums[stack[0]])
        # 窗口开始移动的计算
        for index in range(k, len(nums)):
            # 判断窗口移动后最大的元素是不是出了窗口
            if stack and stack[0] == index - k:
                stack.popleft()
            while stack and nums[stack[-1]] < nums[index]:
                # 窗口内，在该值的后面有比这个值大的值存在，所以该值没有存在的必要，这样可以保障有序，而且左边的值是窗口内最大的元素的索引~
                stack.pop()
            stack.append(index)
            result.append(nums[stack[0]])
        return result

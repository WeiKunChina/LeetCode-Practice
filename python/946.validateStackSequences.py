class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        新建一个辅助栈模拟整个 push 和 pop 的过程来测试是否成功
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        count = 0
        stack = []
        for element in pushed:
            stack.append(element)
            while stack and count < len(popped) and stack[-1] == popped[count]:
                stack.pop()
                count += 1

        return count == len(popped)
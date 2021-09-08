class Solution:
    def balancedStringSplit(self, s: str) -> int:
        """
        贪心：
        根据题意，对于一个平衡字符串 s，若 s 能从中间某处分割成左右两个子串，若其中一个是平衡字符串，则另一个的 L 和 R 字符的数量必然是相同的，所以也一定是平衡字符串。
        为了最大化分割数量，我们可以不断循环，每次从 s 中分割出一个最短的平衡前缀，由于剩余部分也是平衡字符串，我们可以将其当作 s 继续分割，直至 s 为空时，结束循环。
        :param s:
        :return:
        """
        result, count = 0, 0
        for element in s:
            if element == 'L':
                count += 1
            else:
                count -= 1
            if count == 0:
                result += 1
        return result

class Solution(object):
    """
    循环遍历整个数组，循环中再嵌套四个循环，分别是从左至右，从上至下，从右至左，从下至上这几个方向，按照题意将整个数组遍历完成，控制好边界
    m 为行数，nn 为列数，时间复杂度：O(mn)，空间复杂度：O(1)
    """
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []
        answer = []
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) -1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                answer.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                answer.append(matrix[i][right])
            right -= 1
            for i in reversed(range(left, right + 1)):
                answer.append(matrix[bottom][i])
            bottom -= 1
            for i in reversed(range(top, bottom + 1)):
                answer.append(matrix[i][left])
            left += 1
        return answer[:(len(matrix) * len(matrix[0]))]
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#  示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#  示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#  提示：
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 10
#  -100 <= matrix[i][j] <= 100

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
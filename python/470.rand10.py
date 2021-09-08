# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        减少调用次数的情况下，用两次随机数 7 相乘，取前 40 个，转化为 [1,10] 之时，每个数的概率为 4/49
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            number = (row - 1) * 7 + col
            if number <= 40:
                return 1 + (number - 1) % 10

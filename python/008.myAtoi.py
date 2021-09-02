class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        sign = 1
        result = 0
        if not s:
            return 0
        if s[0] == '+':
            sign = 1
            s = s[1:]
        elif s[0] == '-':
            sign = -1
            s = s[1:]

        for c in s:
            if c.isdigit():
                result = result * 10 + int(c)
            else:
                break
        result *= sign
        if result > 2147483647:
            return 2147483647
        if result < -2147483648:
            return -2147483648
        return result

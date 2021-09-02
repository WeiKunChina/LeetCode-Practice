class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        s_list = s.strip().split(' ')
        for i in range(len(s_list)):
            if s_list[len(s_list) - 1 - i] == '':
                continue
            result.append(s_list[len(s_list) - 1 - i])
        return ' '.join(result)

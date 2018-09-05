import re


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        result = re.match(p, s)
        if not result or result.group() != s:
            return False
        elif result.group() == s:
            return True


a = 'ab'
b = '.*c'
s = Solution()
print(s.isMatch(a, b))

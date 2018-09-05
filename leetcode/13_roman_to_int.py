# class Solution:
#     def romanToInt(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         num = 0
#         n = len(s)
#         i = 0
#         while i < n:
#             if s[i] == 'M':
#                 num = num + 1000
#                 i += 1
#             elif s[i] == 'D':
#                 num = num + 500
#                 i += 1
#             elif s[i] == 'C':
#                 if i+1 < n:
#                     if s[i+1] == 'D':
#                         num = num + 400
#                         i += 2
#                     elif s[i+1] == 'M':
#                         num = num + 900
#                         i += 2
#                     else:
#                         num = num + 100
#                         i += 1
#                 else:
#                     num = num + 100
#                     break
#             elif s[i] == 'L':
#                 num = num + 50
#                 i += 1
#             elif s[i] == 'X':
#                 if i+1 < n:
#                     if s[i+1] == 'L':
#                         num = num + 40
#                         i += 2
#                     elif s[i+1] == 'C':
#                         num = num + 90
#                         i += 2
#                     else:
#                         num = num + 10
#                         i += 1
#                 else:
#                     num = num + 10
#                     break
#             elif s[i] == 'V':
#                 num = num + 5
#                 i += 1
#             elif s[i] == 'I':
#                 if i+1 < n:
#                     if s[i+1] == 'V':
#                         num = num + 4
#                         i += 2
#                     elif s[i+1] == 'X':
#                         num = num + 9
#                         i += 2
#                     else:
#                         num += 1
#                         i += 1
#                 else:
#                     num = num + 1
#                     break
#         return num
#
#
# s = Solution()
# print(s.romanToInt("MDLXX"))


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        if len(s) == 1:
            return d[s]
        for i in range(n - 1):
            if d[s[i]] >= d[s[i + 1]]:
                num += d[s[i]]
            else:
                num -= d[s[i]]
        return num + d[s[-1]]
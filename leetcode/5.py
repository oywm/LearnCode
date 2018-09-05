'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。
例如 'abcdcba'
'''

#这里没有考虑到j在temp不行的时候没有j没有返回到最后一位数

# class Solution:
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         d = {'longest': ''}
#         count = 0
#         n = len(s)
#         s_list = []
#         for i in range(n):
#             s1 = ''
#             temp = i
#             for j in range(n):
#                 if temp <= n-(j+1):
#                     if s[temp] == s[n-(j+1)]:
#                         s1 = s1 + s[temp]
#                         if temp == n-(j+1):
#                             s1 = s1 + s1[::-1][1:]
#                             l = len(s1)
#                             if l > len(d['longest']):
#                                 d['longest'] = s1
#                         elif temp+1 == n-(j+1):
#                             s1 = s1 + s1[::-1]
#                             l = len(s1)
#                             if l > len(d['longest']):
#                                 d['longest'] = s1
#                         temp += 1
#
#                     else:
#                         s1 = ''
#                         temp = i
#
#                 else:
#                     s_list.append(s1)
#                     break
#
#         return d['longest']


#时间复杂度太大，有待改进算法，不过最终还是算出来了，只是没有A过
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {'longest': ''}
        n = len(s)
        for i in range(n):
            #j是用来循环遍历的
            j = 0
            #count用来当目前temp不行时，用来返回到当前判断的temp是否相等的位置的。
            count = 0
            s1 = ''
            temp = i
            while j < n:
                if temp <= n-(j+1):
                    if s[temp] == s[n-(j+1)]:
                        count += 1
                        s1 = s1 + s[temp]
                        if temp == n-(j+1):
                            s1 = s1 + s1[::-1][1:]
                            l = len(s1)
                            if l > len(d['longest']):
                                d['longest'] = s1
                        elif temp+1 == n-(j+1):
                            s1 = s1 + s1[::-1]
                            l = len(s1)
                            if l > len(d['longest']):
                                d['longest'] = s1
                        temp += 1
                    else:
                        s1 = ''
                        temp = i
                        j = j - count
                        count = 0

                else:
                    break
                j = j + 1
        return d['longest']


s = Solution()
print(s.longestPalindrome("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))







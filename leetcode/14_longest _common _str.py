class Solution:
    def longestCommonPrefix(self, s):
        """
        :type strs: List[str]
        :rtype: str
        """
        str1 = ''
        n = len(s)
        if not s:
            return str1
        temp = s[0]
        for i in range(n):
            if len(s[i]) <= len(temp):
                temp = s[i]
        m = len(temp)
        print(temp)
        if temp == '':
            return str1
        for i in range(m):
            j = 0
            while j != n:
                if s[j][i] == temp[i]:
                    j += 1
                else:
                    return str1
                if j == n:
                    str1 = str1 + temp[i]
        return str1


s = Solution()
print(s.longestCommonPrefix(["aca","cba"]))



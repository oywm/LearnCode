class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        n = len(digits)
        output = []
        for number in digits:
            output = self.combine(output, dic[number])

        return output

    def combine(self, l1, l2):
        output = []
        if l1 == []:
            return l2
        for temp1 in l1:
            for temp2 in l2:
                output.append(temp1+temp2)

        return output


s = Solution()
print(s.letterCombinations('23'))
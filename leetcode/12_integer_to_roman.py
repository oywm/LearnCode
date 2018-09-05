class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_str = ''
        if num >= 1000:
            for i in range(num // 1000):
                num_str = num_str + 'M'
            num = num % 1000
        if num >= 100:
            if num // 100 < 4:
                for i in range(num // 100):
                    num_str = num_str + 'C'
            elif num // 100 == 4:
                num_str = num_str + 'CD'
            elif num // 100 != 9:
                num_str = num_str + 'D'
                for i in range(num // 100 - 5):
                    num_str = num_str + 'C'
            else:
                num_str = num_str + 'CM'

            num = num % 100
        if num >= 10:
            if num // 10 < 4:
                for i in range(num // 10):
                    num_str = num_str + 'X'
            elif num // 10 == 4:
                num_str = num_str + 'XL'
            elif num // 10 != 9:
                num_str = num_str + 'L'
                for i in range(num//10 - 5):
                    num_str = num_str + 'X'
            else:
                num_str = num_str + 'XC'
            num = num % 10
        if num > 0:
            if num < 4:
                for i in range(num):
                    num_str = num_str + 'I'
            elif num == 4:
                num_str = num_str + 'IV'
            elif num != 9:
                num_str = num_str + 'V'
                for i in range(num- 5):
                    num_str = num_str + 'I'
            else:
                num_str = num_str + 'IX'

        return num_str


s = Solution()
print(s.intToRoman(1994))

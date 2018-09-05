# def twoSum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         if target - nums[i] in nums and i != nums.index(target - nums[i]):
#             return [i, nums.index(target - nums[i])]
#
#
# num = [2, 7, 11, 15]
# target1 = 9
# print(twoSum(num, target1))


class Solution(object):
    def __init__(self):
        self.n = input("请输入一个正整数：")
        self.s = int(input("请输入要去掉几个数字："))
        self.length = len(self.n)

    def solve_problem(self):
        for i in range(self.s):
            for j in range(self.length):
                if j+1 < self.length:
                    if self.n[j] > self.n[j+1]:
                        self.n = (self.n[0:j] + self.n[j+1:])
                        self.length = len(self.n)
                        break
                else:
                    self.n = self.n[0:self.length-1]
                    self.length = len(self.n)
                    break
        return self.n


while True:
    solution = Solution()
    print(solution.solve_problem())

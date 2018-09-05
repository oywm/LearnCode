# class Solution:
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         s = nums[0] + nums[1] + nums[2]
#         if (nums[0] + nums[1] + nums[2] - target) > 0:
#             min1 = nums[0] + nums[1] + nums[2] - target
#         else:
#             min1 = target - (nums[0] + nums[1] + nums[2])
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 for z in range(j + 1, n):
#                     if target == nums[i] + nums[j] + nums[z]:
#                         return nums[i] + nums[j] + nums[z]
#                     elif target > nums[i] + nums[j] + nums[z]:
#                         if min1 >= target - (nums[i] + nums[j] + nums[z]):
#                             min1 = target - (nums[i] + nums[j] + nums[z])
#                             s = nums[i] + nums[j] + nums[z]
#                         else:
#                             pass
#                     else:
#                         if min1 > (nums[i] + nums[j] + nums[z]) - target:
#                             min1 = (nums[i] + nums[j] + nums[z]) - target
#                             s = (nums[i] + nums[j] + nums[z])
#                         else:
#                             pass
#         return s
#
#


# class Solution:
#     def threeSumClosest(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         n = len(nums)
#         l = []
#         for i in range(n):
#             for j in range(i+1, n):
#                 if target > nums[i] + nums[j]:
#                     temp = target - (nums[i] + nums[j])
#                     l.append(temp)
#
#                 else:
#                     temp = -(target - (nums[i] + nums[j]))
#                     l.append(temp)
#
#         l.sort()
#         print(l)
#         for temp in l:
#             if temp in nums:
#                 return temp
#
#
# s = Solution()
# nums = [-3, -2, -5, 3, -4]
# target = -1
# print(s.threeSumClosest(nums, target))

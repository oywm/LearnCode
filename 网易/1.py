# #
# # def binarySearch(nums, target):
# #     low = 0
# #     high = len(nums)-1
# #     midle = (low+high)//2
# #     while low <= high:
# #         if nums[midle] > target:
# #             high = midle - 1
# #             midle = (low+high)//2
# #         elif nums[midle] == target:
# #             if nums[midle] != nums[midle-1]:
# #                 return midle
# #             else:
# #                 high = midle - 1
# #                 midle = (low + high) // 2
# #         elif nums[midle] < target:
# #             low = midle + 1
# #             midle = (low+high)//2
# #         else:
# #             print(nums[midle])
# #             return -1
# #
# #     if nums[low] != target:
# #         return -1
# #
# # a = binarySearch([1,4,4,5,7,7,8,9,9,10],1)
# # print(a)
# #
# #
#
# class Solution:
#     # @param k & A a integer and an array
#     # @return ans a integer
#     def kthLargestElement(self, k, A):
#         n = len(A)
#         k -= 1
#
#         def partitionHelper(s, e):
#             p, q = s + 1, e
#             while p <= q:
#                 if (A[p] > A[s]):
#                     p += 1
#                 else:
#                     A[p], A[q] = A[q], A[p]
#                     q -= 1
#
#             A[s], A[q] = A[q], A[s]
#
#             m = q
#             if m == k:
#                 return A[m]
#             elif m < k:
#                 return partitionHelper(m + 1, e)
#             else:
#                 return partitionHelper(s, m - 1)
#
#         return partitionHelper(0, n - 1)

# class Solution:
#     """
#     @param numbers: Give an array numbers of n integer
#     @return: Find all unique triplets in the array which gives the sum of zero.
#     """


def threeSum(nums):
    l = []
    nums.sort()
    n = len(nums)
    # print(nums)
    for i in range(n):
        for j in range(1, n):
            for z in range(2, n):
                if nums[i] + nums[j] + nums[z] == 0 and i != j and i != z and j != z:
                    if nums[i] >= nums[j] and nums[i] >= nums[z] and nums[j] >= nums[z]:
                        if [nums[z], nums[j], nums[i]] not  in l:
                            l.append([nums[z], nums[j], nums[i]])

                    elif nums[i] >= nums[j] and nums[i] >= nums[z] and nums[z] >= nums[j]:
                        if [nums[j], nums[z], nums[i]] not in l:
                            l.append([nums[j], nums[z], nums[i]])

                    elif nums[i] <= nums[j] and nums[i] >= nums[z]:
                        if [nums[z], nums[i], nums[j]] not in l:
                            l.append([nums[z], nums[i], nums[j]])

                    elif nums[i] >= nums[j] and nums[i] <= nums[z]:
                        if [nums[j], nums[i], nums[z]] not in l:
                            l.append([nums[j], nums[i], nums[z]])

                    elif nums[i] <= nums[j] and nums[j] <= nums[z]:
                        if [nums[i], nums[j], nums[z]] not in l:
                            l.append([nums[i], nums[j], nums[z]])

                    elif nums[i] <= nums[j] and nums[j] >= nums[z] and nums[i] <= nums[z]:
                        if [nums[i], nums[z], nums[j]] not in l:
                            l.append([nums[i], nums[z], nums[j]])

    return l


print(threeSum([1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99,1,2,5,6,7,3,5,8,-33,-5,-72,12,-34,100,99]))

def num(nums):
    nums.sort()
    res = []
    length = len(nums)
    for i in range(0, length - 2):
        if i and nums[i] == nums[i - 1]:
            continue
        target = nums[i] * -1
        left, right = i + 1, length - 1
        while left < right:
            if nums[left] + nums[right] == target:
                res.append([nums[i], nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
    return res
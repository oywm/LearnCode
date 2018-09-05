class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        A.sort()
        A.reverse()
        return A[k-1]


A = [1,2,3,4,5]
k = 1
s = Solution()
print(s.kthLargestElement(k, A))


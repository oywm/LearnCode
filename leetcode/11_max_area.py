class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        p =0
        q = len(height) - 1
        while p != q:
            if height[p] <= height[q]:
                area = height[p] * (q-p)
                p += 1
            elif height[p] > height[q]:
                area = height[q] * (q-p)
                q -= 1
            if max_area < area:
                max_area = area
        print(max_area)
        return max_area


a = [1,2,1]
s = Solution()
s.maxArea(a)
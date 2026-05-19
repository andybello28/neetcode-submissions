class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        ret = 0
        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            if area > ret:
                ret = area
            mini = min(heights[l], heights[r])
            if mini == heights[l] and mini == heights[r]:
                l += 1
            elif mini == heights[l]:
                l += 1
            else:
                r -= 1
        return ret
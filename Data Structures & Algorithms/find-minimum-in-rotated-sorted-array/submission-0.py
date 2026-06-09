class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums) - 1
        m = (r + l) // 2

        #We are just trying to narrow it down in half each time to get to a subarray where it is in order
        while l <= r:
            if nums[l] > nums[r]:
                if nums[m] < nums[l]:
                    r = m
                    m = (r + l) // 2
                if nums[m] > nums[l]:
                    l = m
                    m = (r + l) // 2
                if r - l == 1:
                    return nums[r]

            if nums[l] <= nums[r]:
                return nums[l]
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1


        #We want to find a check to guarantee that our target is still in the subarray we iterate on
        #if our subarray is in order we can easily check if our target is in that range
        #if our subarray is out of order, how do we know?

        while l <= r:
            m = (r + l) // 2

            if nums[m] == target:
                return m

            #left side is in order
            if nums[l] < nums[m]:
                if target in range(nums[l], nums[m] + 1):
                    r = m - 1
                else:
                    l = m + 1

            #right side is in order
            if nums[m] < nums[r]:
                if target in range(nums[m], nums[r] + 1):
                    l = m + 1
                else:
                    r = m - 1

            if nums[l] == nums[m]:
                l = m + 1

        return -1
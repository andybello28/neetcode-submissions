class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        m = (r + l) // 2

        while l <= r:
            if nums[m] == target:
                return m
            #Iterate on the right side
            elif nums[m] < target:
                l = m + 1
                m = (r + l) // 2
            elif nums[m] > target:
                r = m - 1
                m = (r + l) // 2
        
        return -1
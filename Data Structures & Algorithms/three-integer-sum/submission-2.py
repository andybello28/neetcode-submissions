class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        for i in range(len(nums) - 1):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == (-1) * nums[i]:
                    ret.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif nums[left] + nums[right] > (-1) * nums[i]:
                    right -= 1
                else:
                    left += 1

        return ret
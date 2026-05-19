class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        right_array = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_array[i] = 1
            else:
                right_array[i] = right_array[i + 1] * nums[i + 1]
        print(right_array)

        left_array = [0] * len(nums)

        for i in range(0, len(nums)):
            if i == 0:
                left_array[i] = 1
            else:
                left_array[i] = left_array[i-1] * nums[i - 1]
        
        ret = []
        for i in range(len(nums)):
            ret.append(left_array[i] * right_array[i])
        
        return ret

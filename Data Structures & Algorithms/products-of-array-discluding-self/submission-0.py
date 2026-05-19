class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        num_zeros = 0
        for num in nums:
            if num == 0:
                num_zeros += 1
                continue
            product *= num
        
        ret = []
        for i in range(len(nums)):
            if nums[i] == 0:
                if num_zeros == 1:
                    ret.append(int(product))
                else:
                    ret.append(0)                
            else:
                if num_zeros > 0:
                    ret.append(0)
                else:
                    ret.append(int(product / nums[i]))
        return ret
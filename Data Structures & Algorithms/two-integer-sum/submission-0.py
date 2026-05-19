class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for index, num in enumerate(nums):
            search_num = target - num
            small_index = hash.get(search_num, None)
            if small_index != None:
                return [small_index, index]
            if hash.get(num, None) == None:
                hash[num] = index
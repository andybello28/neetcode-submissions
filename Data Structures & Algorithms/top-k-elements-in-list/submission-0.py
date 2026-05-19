class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1

        frequencies = [[] for _ in range(len(nums))]

        for num in hashmap:
            frequencies[hashmap[num] - 1].append(num)
        
        counter = len(nums) - 1
        ret = []
        while len(ret) < k:
            if frequencies[counter] == []:
                counter -= 1
                continue
            else:
                for num in frequencies[counter]:
                    ret.append(num)
                counter -= 1
        
        return ret

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}

        for str in strs:
            count = [0] * 26

            for letter in str:
                count[ord(letter) - ord('a')] += 1

            if tuple(count) not in dict:
                dict[tuple(count)] = [str]
            else:
                dict[tuple(count)].append(str) 
        
        return list(dict.values())
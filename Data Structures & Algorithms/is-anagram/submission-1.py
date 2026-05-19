class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for letter in s:
            if letter in d1:
                d1[letter] += 1
            else:
                d1[letter] = 1

        for letter in t:
            if letter in d2:
                d2[letter] += 1
            else:
                d2[letter] = 1

        return d1 == d2
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, maxLength = 0, 0, 0

        hashset = set()

        while r <= len(s) - 1:
            print(l, r)
            if s[r] not in hashset:
                hashset.add(s[r])
                length = (r - l) + 1
                if length > maxLength:
                    maxLength = length
                r += 1
            else:
                hashset.remove(s[l])
                l += 1
        
        return maxLength
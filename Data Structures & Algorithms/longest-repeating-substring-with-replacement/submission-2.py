class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_length = 0, 0

        frequencies = {}

        for r in range(len(s)):
            frequencies[s[r]] = 1 + frequencies.get(s[r], 0)

            length = r - l + 1

            while length - max(frequencies.values()) > k:
                frequencies[s[l]] -= 1
                l += 1
                length = r - l + 1

            if length > max_length:
                max_length = length
        
        return max_length


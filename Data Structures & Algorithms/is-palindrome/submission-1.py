class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while r > l:
            while not (97 <= ord(s[l]) <= 122 or 48 <= ord(s[l]) <= 57 or 65 <= ord(s[l]) <= 90):
                l += 1
                if l >= r:
                    return True
            while not (97 <= ord(s[r]) <= 122 or 48 <= ord(s[r]) <= 57 or 65 <= ord(s[r]) <= 90):
                r -= 1
                if r < l:
                    return True
            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        
        return True
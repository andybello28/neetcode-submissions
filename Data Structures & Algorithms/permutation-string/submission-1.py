class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0

        count1 = {}
        for letter in s1:
            count1[letter] = 1 + count1.get(letter, 0)

        count2 = {}

        for r in range(len(s2)):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)

            while count2[s2[l]] > count1.get(s2[l], 0) and l < r:
                if count2[s2[l]] == 1:
                    count2.pop(s2[l])
                else:
                    count2[s2[l]] -= 1
                l += 1
            
            print(l, r, count2)

            if count2 == count1:
                return True
        
        return False
        
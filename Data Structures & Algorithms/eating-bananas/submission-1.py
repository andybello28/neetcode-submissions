class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = 0
        for pile in piles:
            if pile > max_pile:
                max_pile = pile

        l = 1
        r = max_pile
        m = (r + l) // 2
        min_k = max_pile

        while l <= r:
            k = m
            time = 0
            for pile in piles:
                if pile <= k:
                    time += 1
                else:
                    if pile % k == 0:
                        time += pile / k
                    else:
                        time += (pile // k) + 1 

            if time > h:
                l = m + 1
                m = (r + l) // 2
            else:
                min_k = m
                r = m - 1
                m = (r + l) // 2


        return min_k

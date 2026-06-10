class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []

        self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key not in self.d:
            return ans
        else:
            array = self.d[key]
            l = 0
            r = len(array) - 1

            while l <= r:
                m = (r + l) // 2

                if array[m][1] < timestamp:
                    ans = array[m][0]
                    l = m + 1
                elif array[m][1] > timestamp:
                    r = m - 1
                else:
                    ans = array[m][0]
                    return ans

            return ans
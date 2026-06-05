class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            #the order in this conditional is a nice way to make sure we don't get indexing errors
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                result[i] = stack[-1] - i
            else:
                result[i] = 0
            
            stack.append(i)
        
        return result

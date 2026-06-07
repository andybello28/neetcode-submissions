class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stack = []

        print(cars)

        for i in range(len(cars) - 1, -1, -1):
            time = (target - cars[i][0]) / cars[i][1]
            if not stack:
                stack.append((cars[i]))
            else:
                fleet_time = (target - stack[-1][0]) / stack[-1][1]
                if time > fleet_time:
                    stack.append(cars[i])
                #It either starts before or at same position
#                if cars[i][0] < stack[-1][0]:

                # else:
                #     if time < fleet_time:
                #         stack.pop()
                #         stack.append(cars[i])

        return len(stack)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeedPairs = []

        for index in range(len(position)):
            positionSpeedPairs.append([position[index], speed[index]])

        stack = []
        for p, s in sorted(positionSpeedPairs)[::-1]:
            time = (target - p) / s
            stack.append(time)
            while len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)
        
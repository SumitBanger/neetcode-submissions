class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPosSpdList = sorted(zip(position, speed))
        stack = []
        for pos, spd in sortedPosSpdList:
            timeToReach = (target - pos) / spd
            while stack and timeToReach >= stack[-1]:
                stack.pop()
            stack.append(timeToReach)
        
        return len(stack)

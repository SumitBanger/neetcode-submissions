class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sortedPosSpdTuples = sorted(zip(position, speed))
        stack = []
        for pos, spd in sortedPosSpdTuples:
            currentCarTimeToTarget = (target - pos) / spd
            while stack and currentCarTimeToTarget >= stack[-1]:
                stack.pop()
            stack.append(currentCarTimeToTarget)
        
        return len(stack)        
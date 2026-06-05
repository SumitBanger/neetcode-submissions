class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result, stack = [0] * len(temperatures), []
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                prevIndex , prevTemp = stack.pop()
                result[prevIndex] = index - prevIndex
            stack.append((index, temperature))
            print(stack)
        
        return result
        
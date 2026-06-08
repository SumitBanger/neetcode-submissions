class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, result = [], [0]*len(temperatures)
        for index, temprature in enumerate(temperatures):
            while stack and temprature > stack[-1][0]:
                topTemp, topIndex = stack.pop()
                result[topIndex] = index - topIndex
            stack.append((temprature,index ))
        
        return result

        
        
        
        
        
        
        
        
        
        
        
        
        result, stack = [0] * len(temperatures), []
        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                prevIndex , prevTemp = stack.pop()
                result[prevIndex] = index - prevIndex
            stack.append((index, temperature))
        
        return result
        
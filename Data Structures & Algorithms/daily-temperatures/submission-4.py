class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, result = [], [0]*len(temperatures)
        for index, temprature in enumerate(temperatures):
            while stack and temprature > stack[-1][0]:
                topTemp, topIndex = stack.pop()
                result[topIndex] = index - topIndex
            stack.append((temprature,index ))
        
        return result
        
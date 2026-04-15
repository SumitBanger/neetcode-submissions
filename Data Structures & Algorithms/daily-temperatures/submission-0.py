class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack, result = [], [0] * len(temperatures)
        stack.append(0)
        for index in range(1, len(temperatures)):
            if stack and temperatures[index] <= temperatures[stack[-1]]:
                stack.append(index)
            else:
                while stack and temperatures[index] > temperatures[stack[-1]]:
                    prevIndex = stack.pop()
                    result[prevIndex] = index - prevIndex
                stack.append(index)

        return result
        
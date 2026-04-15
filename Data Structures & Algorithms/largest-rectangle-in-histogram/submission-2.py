class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        length = len(heights)
        res = 0
        for index in range(length):
            if stack and stack[-1][0] == heights[index]:
                continue
            else:
                start = index
                while stack and stack[-1][0] > heights[index]:
                    currentTopElement = stack.pop()
                    currentHeight = currentTopElement[0]
                    start = currentTopElement[1]
                    currentArea = currentHeight * (index - start)
                    res = max(res, currentArea)
                
                stack.append([heights[index], start])
        
        index = length
        while stack:
            currentTopElement = stack.pop()
            currentHeight = currentTopElement[0]
            start = currentTopElement[1]
            currentArea = currentHeight * (index - start)
            res = max(res, currentArea)

        return res

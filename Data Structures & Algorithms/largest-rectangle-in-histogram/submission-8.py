class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxArea, topIndex = [], 0, 0
        for index, height in enumerate(heights):
            left = index
            while stack and height <= stack[-1][1]:
                topIndex, topHeight = stack.pop()
                maxArea = max(maxArea, topHeight * (index - topIndex))
                left = topIndex
            stack.append((left, height))
        
        print(stack)
        print(maxArea)
        
        while stack:
            topIndex, topHeight = stack.pop()
            maxArea = max(maxArea, topHeight * (len(heights) - topIndex))

        return maxArea
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        stack, maxArea = [], -1
        for index, height in enumerate(heights):
            left = index
            while stack and height <= stack[-1][0]:
                currentHeight, left = stack.pop()
                currentArea = currentHeight * (index - left)
                maxArea = max(maxArea, currentArea)
            stack.append((height, left))

        length = len(heights)
        while stack:
            currentHeight, left = stack.pop()
            currentArea = currentHeight * (length - left)
            maxArea = max(maxArea, currentArea)
        
        return maxArea

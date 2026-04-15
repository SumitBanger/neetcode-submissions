class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        length = len(heights)
        maxArea = 0
        for index in range(length):
            if stack and stack[-1][0] == heights[index]:
                continue
            else:
                start = index
                while stack and stack[-1][0] > heights[index]:
                    currentHeight, start = stack.pop()
                    maxArea = max(maxArea, (currentHeight * (index - start)))
                
                stack.append([heights[index], start])
        
        while stack:
            currentHeight, start = stack.pop()
            maxArea = max(maxArea, (currentHeight * (length - start)))

        return maxArea

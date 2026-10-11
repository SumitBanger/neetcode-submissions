class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack, maxArea = [], 0
        for index, height in enumerate(heights):
            leftIndex = index
            while stack and height <= stack[-1][1]:
                leftIndex, topHeight = stack.pop()
                maxArea = max(maxArea, topHeight * (index - leftIndex))
            stack.append((leftIndex, height))
        
        while stack:
            leftIndex, topHeight = stack.pop()
            maxArea = max(maxArea, topHeight * (len(heights) - leftIndex))

        return maxArea
        
        # stack, maxArea = [], -1
        # for index, height in enumerate(heights):
        #     left = index
        #     while stack and height <= stack[-1][0]:
        #         currentHeight, left = stack.pop()
        #         currentArea = currentHeight * (index - left)
        #         maxArea = max(maxArea, currentArea)
        #     stack.append((height, left))

        # length = len(heights)
        # while stack:
        #     currentHeight, left = stack.pop()
        #     currentArea = currentHeight * (length - left)
        #     maxArea = max(maxArea, currentArea)
        
        # return maxArea

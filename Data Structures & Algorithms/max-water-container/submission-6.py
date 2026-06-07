class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, maxTillNow = 0, len(heights) - 1, 0
        while left < right:
            currentWater = min(heights[left], heights[right]) * (right - left)
            maxTillNow = max(maxTillNow, currentWater)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return maxTillNow




        
        
        
        
        
        
        
        
        
        maxTillNow, left, right = 0, 0, len(heights) - 1
        while left < right:
            currentWater = min(heights[left], heights[right]) * (right - left)
            maxTillNow = max(maxTillNow, currentWater)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxTillNow
        
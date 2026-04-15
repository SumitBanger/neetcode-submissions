class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        waterStored, left, right = 0, 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]

        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])
                #currentWater = 
                waterStored += maxLeft - height[left]
            else: 
                right -= 1
                maxRight = max(maxRight, height[right])
                #currentWater = maxRight - height[right]
                waterStored += maxRight - height[right]

        return waterStored
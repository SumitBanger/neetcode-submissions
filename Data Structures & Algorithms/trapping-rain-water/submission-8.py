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
                currentWater = maxLeft - height[left]
                waterStored += currentWater if currentWater > 0 else 0
            else: 
                right -= 1
                maxRight = max(maxRight, height[right])
                currentWater = maxRight - height[right]
                waterStored += currentWater if currentWater > 0 else 0

        return waterStored
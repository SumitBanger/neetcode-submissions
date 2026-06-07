class Solution:
    def trap(self, height: List[int]) -> int:
        totalBars = len(height)
        waterStored, left, right = 0, 0, totalBars - 1
        maxLeft, maxRight = height[left], height[right]
        while left < right:
            if maxLeft <= maxRight:
                left += 1
                currentWater = maxLeft - height[left]
                maxLeft = max(maxLeft, height[left])
            else:
                right -= 1
                currentWater = maxRight - height[right]
                maxRight = max(maxRight, height[right])
            
            waterStored += currentWater if currentWater >=0 else 0

        return waterStored


        
        
        
        maxTillNowFromEnd, maxTillNow = [0] * totalBars, 0
        for index in range(totalBars - 1, -1, -1):
            maxTillNowFromEnd[index] = maxTillNow
            maxTillNow = max(maxTillNow, height[index])

        maxTillNow, waterStored = 0, 0
        for index, currentHeight in enumerate(height):
            currentWater = min(maxTillNow, maxTillNowFromEnd[index]) - currentHeight
            waterStored += currentWater if currentWater >=0 else 0
            maxTillNow = max(maxTillNow, height[index])
        
        return waterStored


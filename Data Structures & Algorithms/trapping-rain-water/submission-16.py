class Solution:
    def trap(self, height: List[int]) -> int:
        totalBars = len(height)
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

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        maxHeightTillNow, maxHeightFromBack = 0, [0] * len(height)
        for index in range(len(height) - 1, -1, -1):
            maxHeightFromBack[index] = maxHeightTillNow
            maxHeightTillNow = max(maxHeightTillNow, height[index])

        waterStored, maxHeightTillNow = 0, 0
        for index, currentHeight in enumerate(height):
            minHeight = min(maxHeightTillNow, maxHeightFromBack[index])
            # if currentHeight < minHeight:
            #     waterStored += (minHeight - currentHeight)
            waterStored += 0 if currentHeight > minHeight else (minHeight - currentHeight)
            maxHeightTillNow = max(maxHeightTillNow, currentHeight)
        
        return waterStored


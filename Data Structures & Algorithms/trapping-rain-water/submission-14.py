class Solution:
    def trap(self, height: List[int]) -> int:
        maxHeightTillNow, maxHeightFromBack = 0, [0] * len(height)
        for index in range(len(height) - 1, -1, -1):
            maxHeightFromBack[index] = maxHeightTillNow
            maxHeightTillNow = max(maxHeightTillNow, height[index])

        waterStored, maxHeightTillNow = 0, 0
        for index, currentHeight in enumerate(height):
            minHeight = min(maxHeightTillNow, maxHeightFromBack[index])
            if currentHeight < minHeight:
                waterStored += (minHeight - currentHeight)
            maxHeightTillNow = max(maxHeightTillNow, currentHeight)
        
        return waterStored


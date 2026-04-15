class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft, maxRight, waterStored = [0], [0], 0
        temp = 0
        #maxLeft.append(0)
        for i in range(1, len(height)):
            temp = max(temp, height[i-1])
            maxLeft.append(temp)
        
        temp = 0
        #maxRight.insert(0, 0)
        for i in range(len(height) - 2, -1, -1):
            temp = max(temp, height[i+1])
            maxRight.insert(0, temp)

        for i in range(1, len(height) - 1):
            currentWater = min(maxLeft[i], maxRight[i]) - height[i]
            if currentWater > 0:
                waterStored += currentWater

        return waterStored
        
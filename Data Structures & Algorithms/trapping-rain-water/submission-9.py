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

        # 2nd Approach with O(N) extra space
        if not height:
            return 0
        maxLeft, maxRight, waterStored = [0], [0], 0
        temp = 0
        for i in range(1, len(height)):
            temp = max(temp, height[i-1])
            maxLeft.append(temp)
        
        temp = 0
        for i in range(len(height) - 2, -1, -1):
            temp = max(temp, height[i+1])
            maxRight.insert(0, temp)

        for i in range(1, len(height) - 1):
            currentWater = min(maxLeft[i], maxRight[i]) - height[i]
            waterStored += currentWater if currentWater > 0 else 0
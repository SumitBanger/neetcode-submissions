class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, length = set([]), len(nums)
        sortedNums = sorted(nums)

        if sortedNums[0] > 0 or sortedNums[length - 1] < 0:
            return []
        
        for index, targetNum in enumerate(sortedNums):
            left, right = index + 1, length - 1
            while left < right:
                totalSum = targetNum + sortedNums[left] + sortedNums[right]
                if totalSum == 0:
                    res.add((targetNum, sortedNums[left], sortedNums[right]))
                    left += 1
                elif totalSum < 0:
                    left += 1
                elif totalSum > 0:
                    right -= 1
        result = []
        for first, second, third in res:
            result.append([first, second, third])

        return result








        for targetIndex in range(len(sortedNums)):
            target = sortedNums[targetIndex]
            if target > 0:
                break
            left, right = targetIndex + 1, len(sortedNums) - 1
            while left < right:
                threeSum = target + sortedNums[left] + sortedNums[right]
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                elif threeSum == 0:
                    if ([target, sortedNums[left], sortedNums[right]]) not in res:
                        res.append([target, sortedNums[left], sortedNums[right]])
                    right -= 1
        
        return res
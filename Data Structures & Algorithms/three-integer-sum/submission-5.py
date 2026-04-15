class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        sortedNums = sorted(nums)
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
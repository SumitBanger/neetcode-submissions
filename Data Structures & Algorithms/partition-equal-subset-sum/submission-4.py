class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, totalSum = len(nums), sum(nums)
        if total == 1 or totalSum % 2 == 1: # totalSum is odd Or total count is 1
            return False
        targetSum = totalSum // 2

        dp = {}

        def isPossible(i, target):
            if target == 0:
                dp[(i, target)] = True
            if i == total:
                dp[(i, target)] = False
            
            if (i, target) in dp: return dp[(i, target)]
            
            pick = False
            if nums[i] <= target:
                pick = isPossible(i+1, target - nums[i])
            notPick = isPossible(i+1, target)
            dp[(i, target)] = pick or notPick
            return dp[(i, target)]

        return isPossible(0, targetSum)

        
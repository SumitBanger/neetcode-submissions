class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, totalSum = len(nums), sum(nums)
        if total == 1 or totalSum % 2 == 1: # totalSum is odd Or total count is 1
            return False
        targetSum = totalSum // 2

        dp = 1 
        for num in nums:
            # Shift dp left by 'num' positions (adds 'num' to all current sums)
            # and combine it with previous reachable sums using bitwise OR
            dp |= (dp << num)
            # Early exit: check if targetSum bit is set to 1
            if (dp >> targetSum) & 1:
                return True 
        return False

        # dp = [True] + [False]*(targetSum)

        # for num in nums:
        #     for target in range(targetSum, num - 1, -1):
        #         dp[target] = dp[target] or dp[target - num]
        # return dp[targetSum]
        # dp = {}

        '''
        Bounds: i: [0, total], target: [0, targetSum]
        Order: 
            - i: big before small - [total, 0]
            - target: small before big - [0, targetSum]
        BaseCase: i == total: False, target == 0: True
        '''
        # dp = [[False]*(targetSum+1) for _ in range(total+1)]
        # for i in range(total):
        #     dp[i][0] = True



        # def isPossible(i, target):
        #     if target == 0:
        #         dp[(i, target)] = True
        #     if i == total:
        #         dp[(i, target)] = False
            
        #     if (i, target) in dp: return dp[(i, target)]
            
        #     pick = False
        #     if nums[i] <= target:
        #         pick = isPossible(i+1, target - nums[i])
        #     notPick = isPossible(i+1, target)
        #     dp[(i, target)] = pick or notPick
        #     return dp[(i, target)]
        # return isPossible(0, targetSum)

        
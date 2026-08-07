class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total, totalSum = len(nums), sum(nums)
        if total == 1 or totalSum % 2 == 1: # totalSum is odd Or total count is 1
            return False
        targetSum = totalSum // 2
        dp = {}

        '''
        Bounds: i: [0, total], target: [0, targetSum]
        Order: 
            - i: big before small - [total, 0]
            - target: small before big - [0, targetSum]
        BaseCase: i == total: False, target == 0: True
        '''
        dp = [[False]*(targetSum+1) for _ in range(total+1)]
        for i in range(total):
            dp[i][0] = True

        dp_i1 = [True] + [False]*(targetSum)

        for i in range(total - 1, -1, -1):
            dp_i = list(dp_i1)
            for target in range(1, targetSum+1):
                if nums[i] <= target:
                    dp_i[target] |= dp_i1[target - nums[i]]
            dp_i1 = dp_i
        return dp_i1[targetSum]

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

        
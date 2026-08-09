class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # total, totalSum = len(nums), sum(nums)
        # dp = {}
        # # for currSum in range(-1000, 1001):
        # #     dp[(total, currSum)] = 1 if currSum == target else 0

        # for i in range(total, -1, -1):
        #     for currSum in range(-totalSum, totalSum+1):
        #         if i == total:
        #             dp[(i, currSum)] = 1 if currSum == target else 0
        #             continue
        #         pos = dp.get((i+1, currSum+nums[i]), 0)
        #         neg = dp.get((i+1, currSum-nums[i]), 0)
        #         dp[(i, currSum)] = pos + neg
        # return dp.get((0, 0), 0)

        total = len(nums)
        dp = {}
        def num_ways(i, currSum):
            if i == total:
                dp[(i, currSum)] = 1 if currSum == target else 0
            
            if (i, currSum) in dp: return dp[(i, currSum)]
            
            pos = num_ways(i+1, currSum+nums[i])
            neg = num_ways(i+1, currSum-nums[i])
            dp[(i, currSum)] = pos + neg
            return dp[(i, currSum)]
        return num_ways(0, 0)

            

        
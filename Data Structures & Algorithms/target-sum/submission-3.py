class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = len(nums)
        dp = {}

        # for i in range(total, -1, -1):
        #     for currSum in range(target+1):
        #         pos = dp[(i+1, currSum+nums[i])]
        #         neg = dp[(i+1, currSum-nums[i])]
        #         dp[(i, currSum)] = pos + neg

        def num_ways(i, currSum):
            if i == total:
                dp[(i, currSum)] = 1 if currSum == target else 0
            
            if (i, currSum) in dp: return dp[(i, currSum)]
            
            pos = num_ways(i+1, currSum+nums[i])
            neg = num_ways(i+1, currSum-nums[i])
            dp[(i, currSum)] = pos + neg
            return dp[(i, currSum)]
        return num_ways(0, 0)

            

        
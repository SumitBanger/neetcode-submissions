class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        total = len(nums)
        dp = [1] * total
        for i in range(total - 1, -1, -1):
            for j in range(i+1, total):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)
        # dp = {}
        # def get_LIS_length(i, prevMax):
        #     if i == total:
        #         dp[(i, prevMax)] = 0
        #     if (i, prevMax) in dp: return dp[(i, prevMax)]
        #     pick = 0
        #     if nums[i] > prevMax:
        #         pick = 1 + get_LIS_length(i+1, nums[i])
            
        #     skip = 0 + get_LIS_length(i+1, prevMax)
        #     dp[(i, prevMax)] = max(pick, skip)
        #     return dp[(i, prevMax)]
        
        # return get_LIS_length(0, -1001)
        #return dp[0]

        
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        total = len(nums)
        dp = {}
        def get_LIS_length(i, prevMax):
            if i == total:
                dp[(i, prevMax)] = 0
            if (i, prevMax) in dp: return dp[(i, prevMax)]
            pick = 0
            if nums[i] > prevMax:
                pick = 1 + get_LIS_length(i+1, nums[i])
            
            skip = 0 + get_LIS_length(i+1, prevMax)
            dp[(i, prevMax)] = max(pick, skip)
            return dp[(i, prevMax)]
        
        return get_LIS_length(0, -1001)
        #return dp[0]

        
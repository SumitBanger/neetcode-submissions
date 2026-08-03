class Solution:
    def rob(self, nums: List[int]) -> int:
        total = len(nums)
        '''
        Bound: [0, total - 1], dp[total] size
        Order: small before big -> for 0 to total
        Base Cases: dp[0] = nums[0] (no other choice), dp[1] = max(nums[0], nums[1])
        '''
        if total <= 1:
            return nums[0]
        # dp = [0] * total
        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # for i in range(2, total):
        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        # return dp[total -1]

        prevToPrev, prev = nums[0], max(nums[0], nums[1])
        # for i in range(2, total):
        #     current = max(nums[i] + prevToPrev, prev)
        #     prevToPrev, prev = prev, current
        # return prev

        for num in nums[2: total]:
            current = max(num + prevToPrev, prev)
            prevToPrev, prev = prev, current
        return prev


        
        
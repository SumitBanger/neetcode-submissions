class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        total = len(coins)
        dp = [[0] * (amount + 1) for i in range(total)] # dp[i][amount + 1]
        for i in range(total):
            dp[i][0] = 0
        
        for target in range(0, amount + 1):
            dp[0][target] = (target // coins[0]) if target % coins[0] == 0 else (amount + 10)
        
        for i in range(1, total): # start from 1 as all 0 values are pre-computed
            for target in range(0, amount + 1):
                dp[i][target] = dp[i-1][target] # Not Take Case
                take = (amount + 10) # Default Take Case
                if coins[i] <= target:
                    take = 1 + dp[i][target - coins[i]]
                dp[i][target] = min(take, dp[i][target])
        result = dp[total - 1][amount]
        return -1 if result > amount else result

        '''
        Bounds: 
            i: [0, total - 1]
            target: [0, amount]
        Order: 
            i: small before big - [0 to total - 1] 
            target: small before big - [0 to amount]
        BaseCase: 
            i: i == 0 (Single Coin) - if target % coins[0] == 0: return target // coins[0]
            target: target == 0 (No Amount) return 0
        '''

        # def min_coins(i, target):
        #     if i == 0:
        #         if target % coins[0] == 0: return target // coins[0]
        #         return (amount + 10)
        #     take = (amount + 10)
        #     if coins[i] <= target:
        #         take = 1 + min_coins(i, target - coins[i])
        #     notTake = 0 + min_coins(i-1, target)
        #     return min(take, notTake)
        # result = min_coins(total - 1, amount)
        # return -1 if result > amount else result
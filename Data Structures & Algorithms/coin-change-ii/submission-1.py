class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        total = len(coins)
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
        dp = [[0] * (amount + 1) for _ in range(total)]
        # Base Case
        for target in range(0, amount + 1):
            if target % coins[0] == 0: dp[0][target] = 1

        for i in range(1, total):
            for target in range(amount + 1):
                notTake = dp[i-1][target]
                take = 0
                if coins[i] <= target:
                    take = dp[i][target - coins[i]]
                dp[i][target] = take + notTake

        return dp[total-1][amount]

        # def num_ways(i, target):
        #     if i == 0:
        #         return 1 if target % coins[0] == 0 else 0
        #     notTake = num_ways(i-1, target)
        #     take = 0
        #     if coins[i] <= target:
        #         take = num_ways(i, target - coins[i])
        #     return take + notTake

        # return num_ways(total - 1, amount)
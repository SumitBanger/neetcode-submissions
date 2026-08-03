class Solution:
    def numDecodings(self, s: str) -> int:
        total = len(s)
        '''
        Bound: [0, total] -> dp[total + 1] size
        Order: big before small -> for total to 0
        BaseCase: dp[total] = 1
        '''
        dp = [0] * (total + 1)
        dp[total] = 1
        for i in range(total - 1, -1, -1):
            dp[i] = dp[i+1]
            if s[i] == '0':
                dp[i] = 0
                continue
            if i+1 < total and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        return dp[0]

        # dp = { total: 1 }
        # def num_ways(i):
        #     if i in dp: return dp[i]
        #     if s[i] == '0':
        #         return 0
        #     pick = num_ways(i+1)
        #     not_pick = 0
        #     if i+1 < total and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
        #         not_pick = num_ways(i+2)
        #     dp[i] = pick + not_pick
        #     return dp[i]
        # return num_ways(s, 0)
        
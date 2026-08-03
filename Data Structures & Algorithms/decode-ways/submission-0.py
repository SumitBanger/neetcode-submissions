class Solution:
    def numDecodings(self, s: str) -> int:
        total = len(s)
        dp = { total: 1 }

        def num_ways(s, i):
            if i in dp: return dp[i]
            if s[i] == '0':
                return 0
            pick = num_ways(s, i+1)
            not_pick = 0
            if i+1 < total and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                not_pick = num_ways(s, i+2)
            dp[i] = pick + not_pick
            return dp[i]
        
        return num_ways(s, 0)
        
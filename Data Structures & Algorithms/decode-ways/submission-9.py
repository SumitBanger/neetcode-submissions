class Solution:
    def numDecodings(self, s: str) -> int:
        total = len(s)
        '''
        Possibilities:
            - Take [i]th Digit & Convert to Char
                - Digit != 0 for us to take
                - Then solve recursively for remaining digits -> [i+1] to end
            - Skip taking [i]th Digit and Group with next digits
                - As we've max 26 Digits so we can't group more than 2 digits
                - Max Grouped Digit = 26 so Grouped Digits <= 26
                - If 1st Digit = 1, Next Digit Can be any possible digit in [0,9]
                - If 1st Digit = 2, Next Digit <= 6 i.e should be in [0,6]
                - As we group 2 digits - [i],[i+1], so solve recursively for remaining digits -> [i+2] to end

        Bound: [0, total] -> dp[total + 1] size
        Order: big before small -> for total to 0
        BaseCase: dp[total] = 1
        '''
        dp = { total: 1 }

        def num_ways(i):
            if i in dp: return dp[i]
            # if i >= total: return 1
            if s[i] == '0': return 0
            take = num_ways(i+1)
            notTake = 0
            if i+1 < total and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
                notTake = num_ways(i+2)
            dp[i] = take + notTake
            return dp[i]
        
        return num_ways(0)






        # nex, nexToNext = 1, 0
        # for i in range(total - 1, -1, -1):
        #     if s[i] == '0':
        #         current = 0
        #     else:
        #         current = nex
        #     if i+1 < total and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
        #         current += nexToNext
        #     nexToNext = nex
        #     nex = current
            
        # return nex


        # dp = [0] * (total + 1)
        # dp[total] = 1
        # for i in range(total - 1, -1, -1):
        #     if s[i] == '0':
        #         dp[i] = 0
        #         continue
        #     dp[i] = dp[i+1]
        #     if i+1 < total and (s[i] == '1' or (s[i] == '2' and s[i+1] in "0123456")):
        #         dp[i] += dp[i+2]
        # return dp[0]

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
        
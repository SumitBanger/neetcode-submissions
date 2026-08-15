class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sLen, tLen = len(s), len(t)
        dp = {}
        '''
        Bounds: i: [0, sLen], j: [0, tLen]
        Order: 
            - i: big before small - for [sLen to 0]
            - j: big before small - for [tLen to 0]
        BaseCase: 
            - ptr in s String reaches end before ptr in t string -> 0 matches
            - ptr in t String reaches end (pos of ptr in string s no matter) -> 1 matches
        '''
        dp = [[0] * (tLen + 1) for _ in range(sLen+1)]
        for i in range(sLen, -1, -1):
            for j in range(tLen, -1, -1):
                if i == sLen and j < tLen:
                    dp[i][j] = 0
                    continue
                if j == tLen:
                    dp[i][j] = 1
                    continue
                match, no_match = 0, 0
                if s[i] == t[j]:
                    match = dp[i+1][j+1] + dp[i+1][j]
                else:
                    no_match = dp[i+1][j]
                dp[i][j] = match + no_match
        return dp[0][0]

        # def num_dist_seq(i, j):
        #     if i == sLen and j < tLen:
        #         dp[(i,j)] = 0
        #     if j == tLen:
        #         dp[(i,j)] = 1

        #     if (i,j) in dp: return dp[(i,j)]

        #     match, no_match = 0, 0
        #     if s[i] == t[j]:
        #         match = num_dist_seq(i+1, j+1) + num_dist_seq(i+1, j)
        #     else:
        #         no_match = num_dist_seq(i+1, j)
        #     dp[(i,j)] = match + no_match
        #     return dp[(i,j)]
        # return num_dist_seq(0, 0)
        
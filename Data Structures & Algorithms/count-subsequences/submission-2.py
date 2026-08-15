class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sLen, tLen = len(s), len(t)
        if sLen < tLen: return 0
        if s == t: return 1
        dp = {}

        def num_dist_seq(i, j):
            if i == sLen and j < tLen:
                dp[(i,j)] = 0
            if j == tLen:
                dp[(i,j)] = 1

            if (i,j) in dp: return dp[(i,j)]

            match, no_match = 0, 0
            if s[i] == t[j]:
                match = num_dist_seq(i+1, j+1) + num_dist_seq(i+1, j)
            else:
                no_match = num_dist_seq(i+1, j)
            dp[(i,j)] = match + no_match
            return dp[(i,j)]

        return num_dist_seq(0, 0)
        
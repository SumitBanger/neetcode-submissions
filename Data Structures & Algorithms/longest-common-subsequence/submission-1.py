class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1, len2 = len(text1), len(text2)
        dp = [[-1] * (len2+1) for _ in range(len1+1)]

        def lcs_length(ind1, ind2):
            if ind1 == len1 or ind2 == len2:
                dp[ind1][ind2] = 0
            
            if dp[ind1][ind2] != -1: return dp[ind1][ind2]
            
            if text1[ind1] == text2[ind2]:
                dp[ind1][ind2] = 1 + lcs_length(ind1+1, ind2+1)
            else:
                dp[ind1][ind2] = max(lcs_length(ind1+1, ind2), lcs_length(ind1, ind2+1))
            
            return dp[ind1][ind2]
        
        return lcs_length(0, 0)
        
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # len1, len2 = len(text1), len(text2)
        # dp = [[-1] * (len2+1) for _ in range(len1+1)]
        # '''
        # Bounds: ind1: [0, len1], ind2: [0, len2]
        # Order:
        #     - ind1: big before small [len1, 0]
        #     - ind2: big before small [len2, 0]
        # BaseCase: ind1 == len1 or ind2 == len2: dp[ind1][ind2] = 0
        # '''
        # for ind1 in range(len1, -1, -1):
        #     for ind2 in range(len2, -1, -1):
        #         if ind1 == len1 or ind2 == len2:
        #             dp[ind1][ind2] = 0
        #             continue
        #         if text1[ind1] == text2[ind2]:
        #             dp[ind1][ind2] = 1 + dp[ind1+1][ind2+1]
        #         else:
        #             dp[ind1][ind2] = max(dp[ind1+1][ind2], dp[ind1][ind2+1])
        # return dp[0][0]

        '''
        For Space optimisation of above Approach
        We can say: dp[ind1+1] = nextRow, dp[ind1] = currRow 
            - These are the only 2 Rows we need not all the ROWS
        '''
        if len(text1) < len(text2): # Swap if Text1 is Shorter so that Text2 is Shorter O(len(Text2))
            text1, text2 = text2, text1

        len1, len2 = len(text1), len(text2)
        nextRow, currRow = [0] * (len2+1), [0] * (len2+1)
        for ind1 in range(len1 - 1, -1, -1):
            for ind2 in range(len2 - 1, -1, -1):
                if text1[ind1] == text2[ind2]:
                    currRow[ind2] = 1 + nextRow[ind2+1]
                else:
                    currRow[ind2] = max(nextRow[ind2], currRow[ind2+1])
            nextRow = currRow[:]
        return nextRow[0]

        # def lcs_length(ind1, ind2):
        #     if ind1 == len1 or ind2 == len2:
        #         dp[ind1][ind2] = 0
            
        #     if dp[ind1][ind2] != -1: return dp[ind1][ind2]
            
        #     if text1[ind1] == text2[ind2]:
        #         dp[ind1][ind2] = 1 + lcs_length(ind1+1, ind2+1)
        #     else:
        #         dp[ind1][ind2] = max(lcs_length(ind1+1, ind2), lcs_length(ind1, ind2+1))
        #     return dp[ind1][ind2]
        # return lcs_length(0, 0)
        
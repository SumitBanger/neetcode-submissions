class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = m = i = j = 0
        len1, len2, len3 = len(s1), len(s2), len(s3)

        if len1 == len2 == len3 == 0: return True
        if len3 != (len1 + len2): return False

        # dp = [[False] * (len2+1) for _ in range(len1+1)]
        # dp[len1][len2] = True

        nextRow = [False] * (len2+1)
        nextRow[len2] = True
        for j in range(len2 - 1, -1, -1):
            if s2[j] == s3[len1 + j]:
                nextRow[j] = nextRow[j + 1]
        for i in range(len1-1, -1, -1):
            currRow = [False] * (len2+1)
            for j in range(len2, -1, -1):
                if i < len1 and s1[i] == s3[i+j] and nextRow[j]:
                    currRow[j] = True
                if j < len2 and s2[j] == s3[i+j] and currRow[j+1]:
                    currRow[j] = True
            nextRow = currRow[:]
        return nextRow[0]

        # dp = {}
        # def isPossible(i, j):
        #     if i == len1 and j == len2:
        #         return True
        #     if (i, j) in dp: return dp[(i, j)]
        #     if i < len1 and s1[i] == s3[i+j] and isPossible(i+1, j):
        #         return True
        #     if j < len2 and s2[j] == s3[i+j] and isPossible(i, j+1):
        #         return True
        #     dp[(i, j)] = False
        #     return dp[(i, j)]
        # return isPossible(0, 0)



        
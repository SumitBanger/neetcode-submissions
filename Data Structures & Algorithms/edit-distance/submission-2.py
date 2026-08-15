class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        len1, len2 = len(word1), len(word2)
        if word1 == word2: return 0

        dp = {}
        def min_ops(i, j):
            # Base case 1: word1 is exhausted, must insert remaining word2 chars
            if i == len1:
                dp[(i, j)] = len2 - j
            # Base case 2: word2 is exhausted, must delete remaining word1 chars
            if j == len2:
                dp[(i, j)] = len1 - i
            if (i, j) in dp: 
                return dp[(i, j)]

            if i < len1 and word1[i] == word2[j]:
                dp[(i, j)] = min_ops(i+1, j+1)
            else:
                dp[(i, j)] = 1 + (min(min_ops(i, j+1), # insert
                    min_ops(i+1, j+1), # replace
                    min_ops(i+1, j))) # delete
            return dp[(i, j)]
        return min_ops(0, 0)
        
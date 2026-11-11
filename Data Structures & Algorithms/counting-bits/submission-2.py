class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0: return [0]
        dp = [0] * (n+1)
        dp[1], offset = 1, 1
        for i in range(2, n+1):
            if i & (i - 1) == 0: # If i is power of 2 then reset the offset
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp


    #     res = []
    #     for i in range(n+1):
    #         res.append(self.hammingWeight(i))
    #     return res
    
    # def hammingWeight(self, n: int) -> int:
    #     res = 0
    #     while n:
    #         n &= (n - 1)
    #         res += 1
    #     return res
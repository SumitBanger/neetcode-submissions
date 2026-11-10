class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bitToSet = (n >> i) & 1
            res = res | (bitToSet << (31-i))
        return res

        
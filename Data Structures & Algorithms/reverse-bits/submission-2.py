class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            targetBit = (n >> i) & 1
            res |= (targetBit << (31-i))
        return res

        
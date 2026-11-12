class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask in hexadecimal (32 ones)
        mask = 0xFFFFFFFF
        # Maximum positive 32-bit signed integer (0 followed by 31 ones)
        max_int = 0x7FFFFFFF
        res, carry = a, b
        while carry != 0:
            # Calculate carry and mask it to 32 bits
            temp = ((res & carry) << 1) & mask
            # Calculate sum without carry and mask it to 32 bits
            res = (res ^ carry) & mask
            carry = temp
            
        # If res is greater than max_int, the 32nd sign bit is 1 (negative number)
        # Convert it back to Python's negative representation
        return res if res <= max_int else ~(res ^ mask)

        # res, carry = a, b
        # while carry != 0:
        #     temp = (res & carry) << 1
        #     res ^= carry
        #     carry = temp
        # return res
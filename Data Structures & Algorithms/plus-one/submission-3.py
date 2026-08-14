class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if len(digits) == 0:
            return [1]

        output, currSum, carry = [], 0, 1
        for digit in reversed(digits):
            carry, currSum = divmod(digit + carry, 10)
            output.insert(0, currSum)
        output.insert(0, carry) if carry > 0 else None
        return output

        
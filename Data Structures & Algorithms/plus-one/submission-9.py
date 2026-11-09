class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Iterate backwards from the last digit
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits # Best case: O(1) time if last digit isn't 9
            digits[i] = 0
            
        # Worst case: If the loop finishes, it means it was all 9s (e.g., [9,9,9])
        # We prepend a 1 to the front
        return [1] + digits

        ##### SIMPLE AND ELEGANT SOLN BUT NOT OPTIMAL #####
        # if len(digits) == 0: return [1]
        # if digits[-1] != 9: return digits[:-1] + [digits[-1] + 1]
        # return self.plusOne(digits[:-1]) + [0]


        # output, currSum, carry = [], 0, 1
        # for digit in reversed(digits):
        #     carry, currSum = divmod(digit + carry, 10)
        #     output.insert(0, currSum)
        # output.insert(0, carry) if carry > 0 else None
        # return output

        
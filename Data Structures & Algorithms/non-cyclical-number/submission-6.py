class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        slow, fast = n, n
        while True:
            if slow == 1 or fast == 1:
                return True
            slow = self.sumSquareDigits(slow)
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            if slow == fast != 1:
                return False

        # while True:
        #     if n == 1:
        #         return True
        #     if n in visited:
        #         return False
        #     visited.add(n)
        #     n = self.sumSquareDigits(n)

    
    def sumSquareDigits(self, number):
        squareSum = 0
        # for char in str(number):
        #     digit = int(char)
        #     squareSum += digit ** 2
        while number > 0:
            # This replaces both % and // in one clean step
            number, digit = divmod(number, 10)
            squareSum += digit * digit
        return squareSum
        
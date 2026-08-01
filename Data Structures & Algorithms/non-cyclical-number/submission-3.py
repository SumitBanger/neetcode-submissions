class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
            n = self.sumSquareDigits(n)

    
    def sumSquareDigits(self, number):
        squareSum = 0
        for char in str(number):
            digit = int(char)
            squareSum += digit ** 2
        # while number > 0:
        #     digit = number % 10
        #     squareSum += digit * digit
        #     number = number // 10
        return squareSum
        
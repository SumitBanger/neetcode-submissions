class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            n = self.sumSquareDigits(n)
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)

    
    def sumSquareDigits(self, number):
        squareSum = 0
        while number > 0:
            digit = number % 10
            squareSum += digit * digit
            number = number // 10
        return squareSum
        
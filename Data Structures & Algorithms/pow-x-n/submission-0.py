class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Helper function that only worries about positive exponents
        def helper(x: float, n: int) -> float:
            if n == 0: return 1
            
            # Since n is strictly positive, // 2 works perfectly
            res = helper(x, n // 2)
            res *= res
            
            return res * x if n % 2 == 1 else res

        # Handle negative exponent once at the top level
        ans = helper(x, abs(n))
        return ans if n >= 0 else 1 / ans
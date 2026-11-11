class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum, currentSum = (n * (n+1)) >> 1, 0
        for num in nums:
            currentSum += num
        return expectedSum - currentSum
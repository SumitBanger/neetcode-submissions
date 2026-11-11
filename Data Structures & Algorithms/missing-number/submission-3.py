class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # expectedSum = (n * (n+1)) >> 1
        # for num in nums:
        #     currentSum += num
        # return expectedSum - currentSum
        return ((n * (n+1)) >> 1) -  sum(nums)
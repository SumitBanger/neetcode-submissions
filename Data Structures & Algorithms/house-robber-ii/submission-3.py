class Solution:
    def rob(self, nums: List[int]) -> int:
        total = len(nums)
        if total <= 1:
            return nums[0]
        
        return max(self.houseRobber1(nums, 0, total - 1), self.houseRobber1(nums, 1, total))

    def houseRobber1(self, nums: List[int], start, end):
        total = end - start
        if total <= 1:
            return nums[start]
        prevToPrev, prev = nums[start], max(nums[start], nums[start + 1])
        for num in nums[start + 2: end]:
            current = max(num + prevToPrev, prev)
            prevToPrev, prev = prev, current
        return prev
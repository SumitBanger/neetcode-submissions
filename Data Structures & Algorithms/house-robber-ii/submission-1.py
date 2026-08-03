class Solution:
    def rob(self, nums: List[int]) -> int:
        total = len(nums)
        if total <= 1:
            return nums[0]
        
        return max(self.houseRobber1(nums[:total-1]), self.houseRobber1(nums[1:total]))

    def houseRobber1(self, nums: List[int]):
        total = len(nums)
        if total <= 1:
            return nums[0]
        prevToPrev, prev = nums[0], max(nums[0], nums[1])
        for num in nums[2: total]:
            current = max(num + prevToPrev, prev)
            prevToPrev, prev = prev, current
        return prev
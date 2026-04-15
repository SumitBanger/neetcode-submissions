class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            if nums[abs(num)] < 0:
                return abs(num)
            else:
                nums[abs(num)] *= -1

        
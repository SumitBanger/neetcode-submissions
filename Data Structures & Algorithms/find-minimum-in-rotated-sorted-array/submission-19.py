class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            midVal = nums[mid]
            prevIndexVal, nextIndexVal = nums[(mid - 1) % length], nums[(mid + 1) % length]
            if prevIndexVal >= midVal <= nextIndexVal:
                return midVal
            elif nums[left] <= midVal >= nums[right]:
                left = mid + 1
            elif midVal <= nums[right]:
                right = mid - 1
        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        total = len(nums)
        left, right = 0, total - 1
        if total <= 2:
            return min(nums)
        while left <= right:
            mid  = (left + right) // 2
            val = nums[mid]
            if val <= nums[(mid + 1) % total] and val <= nums[(mid - 1) % total]:
                return val
            elif val >= nums[left] and val >= nums[right]:
                left = mid + 1
            elif val <= nums[right]:
                right = mid - 1
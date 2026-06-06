class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            midVal = nums[mid]
            if target == midVal:
                return mid
            elif nums[left] <= midVal >= nums[right]:
                if nums[left] <= target < midVal:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target > midVal:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
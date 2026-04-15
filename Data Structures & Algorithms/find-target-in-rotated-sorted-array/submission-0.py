class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        res = -1
        while left <= right:
            mid = (left + right) // 2
            midVal = nums[mid]
            if midVal == target:
                res = mid
                break
            elif midVal >= nums[left] and midVal >= nums[right]:
                if target >= nums[left] and target < midVal:
                    right = mid - 1
                else:
                    left = mid + 1
            elif midVal <= nums[right]:
                if target <= nums[right] and target > midVal:
                    left = mid + 1
                else:
                    right = mid - 1
            
        return res
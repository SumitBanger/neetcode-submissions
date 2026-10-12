class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left, right = 0, length - 1
        while left <= right:
            mid = (left + right) // 2
            midVal, midLeftVal, midRightVal = nums[mid], nums[(mid - 1) % length], nums[(mid + 1) % length]

            if midLeftVal >= midVal <= midRightVal:
                return midVal
            elif nums[left] <= midVal >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1      
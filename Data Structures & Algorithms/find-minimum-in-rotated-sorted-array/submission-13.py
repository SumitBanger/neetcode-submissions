class Solution:
    def findMin(self, nums: List[int]) -> int:
        numsLen = len(nums)
        left, right = 0, numsLen - 1
        if numsLen <= 2:
            return min(nums)
        
        while left <= right:
            mid = (left + right) // 2
            midVal = nums[mid]
            if midVal <= nums[(mid + 1) % numsLen] and midVal <= nums[(mid - 1) % numsLen]:
                return midVal
            elif midVal >= nums[left] and  midVal >= nums[right]:
                left = mid + 1
            elif midVal <= nums[right]:
                right = mid - 1
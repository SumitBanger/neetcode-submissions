class Solution:
    def findMin(self, nums: List[int]) -> int:
        length = len(nums)
        left, right, result = 0, length - 1, -1
        while left <= right:
            mid = (left + right) // 2
            midVal = nums[mid]
            prevValue, nextValue = nums[(mid - 1) % length], nums[(mid + 1) % length]

            if midVal <= prevValue and midVal <= nextValue:
                return midVal
            elif midVal >= nums[left] and midVal >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1




        
        
        
        
        
        
        
        
        
        
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
            else:
                right = mid - 1
        
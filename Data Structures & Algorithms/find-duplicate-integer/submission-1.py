class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        
        
        # This solution although not uses extra space but modifies original array so not optimal
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            else:
                nums[abs(num)] *= -1

        
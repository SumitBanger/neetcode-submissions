class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0

        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        
        fast = 0
        while True:
            slow, fast = nums[slow], nums[fast]
            if slow == fast:
                return slow
        
        
        
        # for num in nums:
        #     if nums[abs(num)] < 0:
        #         return abs(num)
        #     nums[abs(num)] *= -1
        
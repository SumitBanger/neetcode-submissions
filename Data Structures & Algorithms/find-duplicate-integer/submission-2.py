class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break


        #After loop both pointer would be at collision point of both pointers
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
        
        
        # This solution although not uses extra space but modifies original array so not optimal
        for num in nums:
            if nums[abs(num)] < 0:
                return abs(num)
            else:
                nums[abs(num)] *= -1

        
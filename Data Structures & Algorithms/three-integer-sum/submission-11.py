class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = {}
        nums = sorted(nums)
        for index in range(len(nums) - 2):
            left, right = index + 1, len(nums) - 1
            while left < right:
                if nums[index] + nums[left] + nums[right] == 0:
                    result[(nums[index], nums[left], nums[right])] = [nums[index], nums[left], nums[right]]
                    right -= 1
                elif nums[index] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1
        
        return list(result.values())
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid  = (left + right) // 2
            midEle = nums[mid]
            if midEle == target:
                result = mid
                break
            elif midEle < target:
                left = mid + 1
            else:
                right = mid - 1

        return result
        
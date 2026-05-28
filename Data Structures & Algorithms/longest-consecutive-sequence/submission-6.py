class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        result = 0
        for num in nums:
            if (num - 1) not in uniq:
                i = 1
                while (num + i) in uniq:
                    i += 1
                result = max(result, i)
            
        return result


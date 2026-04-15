class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postProduct, temp = {}, 1
        for i in range (len(nums), -1, -1):
            postProduct[i] = temp
            temp *= nums[i-1]

        prev, res = 1, []
        for i in range(len(nums)):
            res.append(prev * postProduct[i + 1])
            prev *= nums[i]
        #res.append(prev)

        return res
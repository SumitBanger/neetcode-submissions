class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productTillNow, frontPassList = 1, []
        for index in range(len(nums)):
            frontPassList.append(productTillNow)
            productTillNow *= nums[index]

        productTillNow, result = 1, [1] * len(nums)
        for index in range(len(nums) - 1, -1, -1):
            result[index] = productTillNow * frontPassList[index]
            productTillNow *= nums[index]
        
        return result

        
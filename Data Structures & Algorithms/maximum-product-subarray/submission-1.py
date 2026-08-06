class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        '''
        ### 2 Solutions are possible for this question ###
        1) Keep Hold of prevMax, prevMin till now + use both while figuring out currMax
            - Intution: 
                A) prevMax can turn to currMax in case current number is +ve
                B) prevMin can turn to currMax in case current number is -ve
        2) Keep Hold of prefix and suffix Product + Max of them would be currMax
            - Intution: (Think about all possible Cases)
                A) All numbers +ve -> Ans: Product of all numbers (prefixProd = suffixProd after loop)
                B) Even -ve numbers -> Ans: Product of all numbers (prefixProd = suffixProd after loop)
                C) Odd -ve numbers -> Ans: Skip one -ve number and Ans = Max(prefixProd, suffixProd) post all possible -ve number skips one by one
                D) In case of 0, reset prefixProd, suffixProd to 1 instead of 0
        '''
        prevMax = prevMin = nums[0]
        result = prevMax
        for curr in nums[1:]:
            currMax = max(curr, curr*prevMax, curr*prevMin)
            currMin = min(curr, curr*prevMax, curr*prevMin)
            #print(f"prevMax: {prevMax}, prevMin:{prevMin}, currMax: {currMax}, currMin: {currMin}")
            prevMax, prevMin = currMax, currMin
            result = max(result, prevMax, prevMin)

        return result
        
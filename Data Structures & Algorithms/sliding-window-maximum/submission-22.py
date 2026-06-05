class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxTillNow_DQ = collections.deque()
        maxTillNow_DQ.append((0, nums[0]))
        for index, num in enumerate(nums[0:k]):
            while maxTillNow_DQ and num >= maxTillNow_DQ[-1][1]:
                if maxTillNow_DQ:
                    maxTillNow_DQ.pop()
            maxTillNow_DQ.append((index, num))
        
        print(f"maxTillNow_DQ: {maxTillNow_DQ}")

        left, result = 0, []
        result.append(maxTillNow_DQ[0][1])
        for right in range(k, len(nums)):
            print(f"maxTillNow_DQ start: {maxTillNow_DQ}")
            if left == maxTillNow_DQ[0][0]:
                print(f"maxTillNow_DQ in IF 1: {maxTillNow_DQ}")
                maxTillNow_DQ.popleft()
            left += 1

            num = nums[right]
            while maxTillNow_DQ and num >= maxTillNow_DQ[-1][1]:
                if maxTillNow_DQ:
                    maxTillNow_DQ.pop()
            maxTillNow_DQ.append((right, num))
            print(f"maxTillNow_DQ end: {maxTillNow_DQ}")
            
            result.append(maxTillNow_DQ[0][1])
            
        return result


        

        
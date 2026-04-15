class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, large = (nums1, nums2) if (len(nums1) <= len(nums2)) else (nums2, nums1)

        m, n, median = len(small), len(large), 0.0
        combinedArrayHalf = (m + n) // 2
        isEven = True if ((m + n) % 2 == 0) else False

        # Run Binary Search on Small Array & find pivot point where we should discard remaining array
        left, right = 0, m - 1
        while True:
            smallArrayMid = (left + right) // 2
            smallArrayMidVal = small[smallArrayMid] if (smallArrayMid >= 0) else float("-infinity")
            smallArrayMidNextVal = small[smallArrayMid + 1] if (smallArrayMid + 1 < m) else float("infinity")
            largeArrayBound = combinedArrayHalf - smallArrayMid - 2
            largeArrayBoundVal = large[largeArrayBound] if (largeArrayBound >= 0) else float("-infinity")
            largeArrayBoundNextVal = large[largeArrayBound + 1] if (largeArrayBound + 1 < n) else float("infinity")

            if smallArrayMidVal <= largeArrayBoundNextVal and largeArrayBoundVal <= smallArrayMidNextVal:
                if not isEven:
                    median = min(smallArrayMidNextVal, largeArrayBoundNextVal)
                else:
                    median = (max(smallArrayMidVal, largeArrayBoundVal) + min(smallArrayMidNextVal, largeArrayBoundNextVal)) / 2
                break
            elif smallArrayMidVal > largeArrayBoundNextVal:
                right = smallArrayMid - 1
            elif largeArrayBoundVal > smallArrayMidNextVal:
                left = smallArrayMid + 1

        return median
   
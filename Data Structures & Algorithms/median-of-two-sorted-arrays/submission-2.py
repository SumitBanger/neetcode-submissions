class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        half = (m + n) // 2
        
        (big, small) = (nums1, nums2) if m >= n else (nums2, nums1)
        left, right = 0, len(small) - 1,
        print(f"small: {small} & big: {big}")
        while True:
            mid = (left + right) // 2
            bigMid = half - mid - 2
            print(f"mid: {mid} & bigMid: {bigMid}")

            smallLeftEnd = small[mid] if mid >= 0 else float("-infinity")
            smallRightStart = small[mid + 1] if mid + 1 < len(small) else float("infinity")
            bigLeftEnd = big[bigMid] if bigMid >= 0 else float("-infinity")
            bigRightStart = big[bigMid + 1] if bigMid + 1 < len(big) else float("infinity")

            if smallLeftEnd <= bigRightStart and bigLeftEnd <= smallRightStart:
                print(f"smallLeftEnd: {smallLeftEnd}, bigRightStart: {bigRightStart}, bigLeftEnd: {bigLeftEnd}, smallRightStart: {smallRightStart}")
                if (m + n) % 2 == 1: # Odd Length Combined Array -> Return Mid Element
                    return min(smallRightStart, bigRightStart)
                else: # Even Length Combined Array -> Return Avrage of both Mid Elements
                    return (max(smallLeftEnd, bigLeftEnd) + min(smallRightStart, bigRightStart)) / 2
            elif smallLeftEnd > bigRightStart:
                right = mid - 1
                print(f"elif - smallLeftEnd: {smallLeftEnd}, bigRightStart: {bigRightStart} - left: {left} & right: {right}")
            else:
                left = mid + 1
                print(f"else - bigLeftEnd: {bigLeftEnd}, smallRightStart: {smallRightStart} - left: {left} & right: {right}")



            
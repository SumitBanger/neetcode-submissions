class Solution:
    def longestPalindrome(self, s: str) -> str:
        strLen = len(s)
        result, resLen = "", 0
        if strLen < 2: return s

        for mid in range(strLen):
            # Odd Length
            left, right = mid, mid # start from same element as mid element
            while left >= 0 and right < strLen and s[left] == s[right]:
                currLen = right - left + 1
                if currLen >= resLen:
                    resLen = currLen
                    result = s[left: right+1]
                left, right = left - 1, right + 1

            # Even Length
            if mid + 1 < strLen and s[mid] != s[mid + 1]: continue
            left, right = mid, mid + 1 # start from 2 mid elements
            while left >= 0 and right < strLen and s[left] == s[right]:
                currLen = right - left + 1
                if currLen >= resLen:
                    resLen = currLen
                    result = s[left: right+1]
                left, right = left - 1, right + 1

        return result
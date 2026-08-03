class Solution:
    def countSubstrings(self, s: str) -> int:
        strLen = len(s)
        result = 0
        if strLen < 2: return 1

        for mid in range(strLen):
            # Odd Length
            # left, right = mid, mid # start from same element as mid element
            result += self.countPalindromes(s, mid, mid)
            # while left >= 0 and right < strLen and s[left] == s[right]:
            #     result += 1
            #     left, right = left - 1, right + 1

            # Even Length
            # if mid + 1 < strLen and s[mid] != s[mid + 1]: continue
            # left, right = mid, mid # start from 2 mid elements
            result += self.countPalindromes(s, mid, mid + 1)
            # while left >= 0 and right < strLen and s[left] == s[right]:
            #     result += 1
            #     left, right = left - 1, right + 1

        return result

    def countPalindromes(self, s, left, right):
        result = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            left, right = left - 1, right + 1
        return result

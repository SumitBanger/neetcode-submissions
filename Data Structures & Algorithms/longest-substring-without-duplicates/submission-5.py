class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        if len(s) <= 1:
            return len(s)
        
        left, right, maxLength = 0, 1, 1
        seen.add(s[left])
        while left < right < len(s):
            currentChar = s[right]
            if currentChar not in seen:
                seen.add(currentChar)
                maxLength = max(maxLength, len(seen))
                right += 1
                print(f"Inside If: seen: {seen}")
            else:
                while s[left] != currentChar:
                    seen.remove(s[left])
                    left += 1
                    print(f"Inside Else While : seen: {seen}")
                print(f"Inside Else : seen: {seen}")
                maxLength = max(maxLength, len(seen))
                right += 1
                left += 1

        return maxLength
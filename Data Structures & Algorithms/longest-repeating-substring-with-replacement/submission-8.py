class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, maxLength, currentWindowLength, maxCharCount = 0, 0, 0, 0
        count = {}
        for index, char in enumerate(s):
            count[char] = count.get(char,0) + 1

            maxCharCount = max(count.values())  
            currentWindowLength = index - left + 1

            if currentWindowLength - maxCharCount <= k:
                maxLength = max(maxLength, currentWindowLength)
            else:
                count[s[left]] = count.get(s[left],0) - 1
                left += 1

        
        return maxLength
        
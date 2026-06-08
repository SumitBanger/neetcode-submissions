class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, maxChar, charFreqMap, maxLength = 0, s[0], defaultdict(), 0
        for index, char in enumerate(s):
            charFreqMap[char] = charFreqMap.get(char, 0) + 1
            if char != maxChar and charFreqMap[char] > charFreqMap[maxChar]:
                maxChar = char
            currentLength = index - left + 1
            if currentLength - charFreqMap[maxChar] <= k:
                maxLength = max(maxLength, currentLength)
            else:
                charFreqMap[s[left]] -= 1
                left += 1

        return maxLength
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
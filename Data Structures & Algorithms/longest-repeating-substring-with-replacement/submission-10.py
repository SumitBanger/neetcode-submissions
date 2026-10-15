class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count, left, max_freq, max_length = {}, 0, 0, 0
        
        for right, char in enumerate(s):
            # 1. Update the character count
            char_count[char] = char_count.get(char, 0) + 1
            # 2. Track the maximum frequency seen in any window so far
            max_freq = max(max_freq, char_count[char])
            
            # 3. If the current window is invalid, shrink it from the left
            # (Window length minus max_freq gives the number of characters to replace)
            while (right - left + 1) - max_freq > k:
                char_count[s[left]] -= 1
                left += 1
                
            # 4. Update the maximum valid window length found
            max_length = max(max_length, right - left + 1)
            
        return max_length
        


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
        
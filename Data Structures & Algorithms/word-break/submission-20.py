class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        strLen = len(s)
        # def canBeSegmented(i):
        #     if(i == strLen):
        #         return True
        #     isPossible = False
        #     for word in wordDict:
        #         wordLen = len(word)
        #         if i + wordLen <= strLen and s[i: i+wordLen] == word:
        #             isPossible |= canBeSegmented(i+wordLen);
        #             if isPossible: break
        #     return isPossible
        '''
        Bounds: i -> [0, strLen]
        Order: big before small -> [strLen to 0]
        Base Case: dp[strLen] = True as at the end it'd be empty String which is always possible
        '''
        wordSet = set(wordDict) # O(1) lookups
        
        # Track unique lengths of words present in the dictionary to avoid useless slices
        wordLengths = set(len(w) for w in wordDict) 
        
        dp = [False] * strLen + [True]
        
        for i in range(strLen - 1, -1, -1):
            for l in wordLengths:
                if i + l <= strLen and dp[i + l]:
                    if s[i : i + l] in wordSet:
                        dp[i] = True
                        break # Found a valid break, move to next i

        # dp = [False] * (strLen) + [True]
        # for i in range(strLen - 1, -1, -1):
        #     current_char = s[i] # Cache the current character
        #     # Try every word in the dictionary
        #     for word in wordDict:
        #         # Fast check: skip if the first character doesn't even match
        #         if word[0] != current_char:
        #             continue
        #         wordLen = len(word)
        #         # Check if the word fits and matches the current prefix
        #         if i + wordLen <= strLen and s[i : i + wordLen] == word:
        #             # Recursively check the rest of the string
        #             if dp[i + wordLen]:
        #                 dp[i] = True # Exit immediately ONLY if it works!
        #                 break
        return dp[0]

        # def canBeSegmented(i):
        #     # Base case: reached the end of the string successfully
        #     if i in dp: return dp[i] 
        #     dp[i] = False
        #     # Try every word in the dictionary
        #     for word in wordDict:
        #         wordLen = len(word)
        #         # Check if the word fits and matches the current prefix
        #         if i + wordLen <= strLen and s[i : i + wordLen] == word:
        #             # Recursively check the rest of the string
        #             if canBeSegmented(i + wordLen):
        #                 return True # Exit immediately ONLY if it works!
        #                 #break
        #     # If no words in the dictionary lead to a valid segmentation
        #     return dp[i]

        # dp = {strLen: True}
        # def canBeSegmented(i):
        #     # Base case: reached the end of the string successfully
        #     if i in dp: return dp[i] 
        #     dp[i] = False
        #     # Try every word in the dictionary
        #     for word in wordDict:
        #         wordLen = len(word)
        #         # Check if the word fits and matches the current prefix
        #         if i + wordLen <= strLen and s[i : i + wordLen] == word:
        #             # Recursively check the rest of the string
        #             if canBeSegmented(i + wordLen):
        #                 return True # Exit immediately ONLY if it works!
        #                 #break
        #     # If no words in the dictionary lead to a valid segmentation
        #     return dp[i]
            
        # return canBeSegmented(0)
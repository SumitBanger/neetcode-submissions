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

        dp = {strLen: True}
        def canBeSegmented(i):
            # Base case: reached the end of the string successfully
            if i in dp: return dp[i] 
            dp[i] = False
            # Try every word in the dictionary
            for word in wordDict:
                wordLen = len(word)
                
                # Check if the word fits and matches the current prefix
                if i + wordLen <= strLen and s[i : i + wordLen] == word:
                    # Recursively check the rest of the string
                    if canBeSegmented(i + wordLen):
                        dp[i] = True # Exit immediately ONLY if it works!
                        break
            
            # If no words in the dictionary lead to a valid segmentation
            return dp[i]
            
        return canBeSegmented(0)
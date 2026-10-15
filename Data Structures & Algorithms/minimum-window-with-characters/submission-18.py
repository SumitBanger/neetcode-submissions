class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        if len(s) < len(t): return ""
            
        countFreq_T, countFreq_S = {}, {}
        for char in t:
            countFreq_T[char] = countFreq_T.get(char, 0) + 1
            
        left, match = 0, 0
        # Store pointers to track the best window instead of slicing strings
        min_len = float('inf')
        best_left, best_right = 0, 0
        
        for right, currentChar in enumerate(s): 
            countFreq_S[currentChar] = countFreq_S.get(currentChar, 0) + 1
            
            if currentChar in countFreq_T and countFreq_S[currentChar] <= countFreq_T[currentChar]:
                match += 1
                
            if match == len(t):
                leftChar = s[left]
                # Shrink the window from the left as much as possible
                while (leftChar not in countFreq_T) or (countFreq_S[leftChar] > countFreq_T[leftChar]):
                    countFreq_S[leftChar] -= 1
                    left += 1
                    leftChar = s[left]
                
                # Check window size using simple integer math O(1)
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    best_left = left
                    best_right = right
                    
        # Perform the string slice exactly ONCE at the end O(N)
        return s[best_left:best_right+1] if min_len != float('inf') else ""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequencyS, frequencyT = {}, {}
        for c in s:
            frequencyS[c] = frequencyS.get(c,0) + 1
        
        for c in t:
            frequencyT[c] = frequencyT.get(c,0) + 1

        for c in frequencyS:
            if frequencyS[c] != frequencyT.get(c,0):
                return False
            
        return True
        
        return frequencyS == frequencyT
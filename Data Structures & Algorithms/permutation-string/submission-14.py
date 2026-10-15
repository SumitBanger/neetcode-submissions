class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Len, s2Len = len(s1), len(s2)
        if s1Len > s2Len:
            return False

        s1CountsMap, s2InitCountsMap, left = Counter(s1), Counter(s2[:s1Len]), 0
        for right in range(s1Len, s2Len):
            if s1CountsMap == s2InitCountsMap:
                return True
            s2InitCountsMap[s2[left]] -= 1
            # Clean up zero counts to prevent comparison failures
            if s2InitCountsMap[s2[left]] == 0:
                del s2InitCountsMap[s2[left]]
            left += 1
            s2InitCountsMap[s2[right]] += 1
        return s1CountsMap == s2InitCountsMap




        
        countsListS1 = self.getCountsList(s1)
        left, right = 0, len(s1) - 1
        countsListSubStr = self.getCountsList(s2[left:right + 1])
        while right < len(s2):
            if(countsListS1 == countsListSubStr):
                return True
            if right == len(s2) - 1:
                return False
            countsListSubStr[ord(s2[left]) - ord('a')] -= 1
            left += 1
            right += 1
            countsListSubStr[ord(s2[right]) - ord('a')] += 1
            
        return False

    def getCountsList(self, string: str):
        countsList = [0]*26
        for char in string:
            countsList[ord(char) - ord('a')] += 1
        return countsList
        
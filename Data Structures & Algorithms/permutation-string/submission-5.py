class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countsListS1 = self.getCountsList(s1)
        left, right = 0, len(s1)
        while right <= len(s2):
            subStr = s2[left:right]
            countsListSubStr = self.getCountsList(subStr)
            if(countsListS1 == countsListSubStr):
                return True
            left += 1
            right += 1

        return False



    def getCountsList(self, string: str):
        countsList = [0]*26
        for char in string:
            countsList[ord(char) - ord('a')] += 1
        return countsList
        
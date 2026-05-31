class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countsListS1 = self.getCountsList(s1)
        left, right = 0, len(s1) - 1
        countsListSubStr = self.getCountsList(s2[left:right + 1])
        print(countsListS1)
        while right < len(s2):
            print(f"subStr: {s2[left:right + 1]}, \ncountsListSubStr:{countsListSubStr}")
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
        
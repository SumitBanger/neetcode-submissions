class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmapToStrListMap = {}
        for str in strs:
            currentStrCharCountTuple = self.getCharCountListTuple(str)
            if currentStrCharCountTuple in hashmapToStrListMap:
                hashmapToStrListMap[currentStrCharCountTuple].append(str)
            else:
                hashmapToStrListMap[currentStrCharCountTuple] = [str]
        
        return list(hashmapToStrListMap.values())
        
    
    def getCharCountListTuple(self, str):
        charCountList = [0] * 26
        for char in str:
            charCountList[ord(char) - ord('a')] += 1
        
        return tuple(charCountList)
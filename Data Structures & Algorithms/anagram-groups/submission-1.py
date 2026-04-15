class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCountTupleToStrListMap = {}
        for str in strs:
            currentStrCharCountTuple = self.getCharCountListTuple(str)
            if currentStrCharCountTuple in charCountTupleToStrListMap:
                charCountTupleToStrListMap[currentStrCharCountTuple].append(str)
            else:
                charCountTupleToStrListMap[currentStrCharCountTuple] = [str]
        
        return list(charCountTupleToStrListMap.values())
        
    
    def getCharCountListTuple(self, str):
        charCountList = [0] * 26
        for char in str:
            charCountList[ord(char) - ord('a')] += 1
        
        return tuple(charCountList)
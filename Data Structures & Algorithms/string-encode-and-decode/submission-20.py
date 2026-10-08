class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for currString in strs:
            currStrLen = str(len(currString))
            encodedString += currStrLen + '#' + currString
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedList = []
        if s == None or s == "":
            return decodedList
        
        prevStrEndIndex = 0
        while True:
            hashIndex = s.find('#', prevStrEndIndex)
            currStrLen = int(s[prevStrEndIndex: hashIndex])
            currStrStartIndex = hashIndex + 1
            currStrEndIndex = currStrStartIndex + currStrLen
            decodedList.append(s[currStrStartIndex: currStrEndIndex])
            if currStrEndIndex == len(s):
                break
            prevStrEndIndex = currStrEndIndex

        
        return decodedList
        
        
        
        
        
        
        
        
        
        
        
        
        while True:
            hashIndex = s.find('#', endIndex)
            strLen = int(s[endIndex: hashIndex])
            startIndex = hashIndex + 1
            endIndex = startIndex + strLen
            print(f"startIndex: {startIndex}, endIndex: {endIndex}, strLen: {strLen}")
            decodedList.append(s[startIndex: endIndex])
            if endIndex == len(s):
                break
            print(endIndex)

        return decodedList

        
        # j = -1 
        # while True:
        #     i = j+1
        #     j = s.find('#', i)
        #     length = int(s[i: j])
        #     i = j+1
        #     j = j+length
        #     decodedList.append(s[i: j+1])
        #     if(j+1 >= len(s)):
        #         break
        
        # return decodedList



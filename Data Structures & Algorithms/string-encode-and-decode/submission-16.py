class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + '#' + string
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedList = []
        if s == None or s == "":
            return decodedList
        
        endIndex = 0
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



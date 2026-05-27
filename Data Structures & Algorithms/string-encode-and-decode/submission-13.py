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
        j = -1 
        while True:
            i = j+1
            j = s.find('#', i)
            length = int(s[i: j])
            i = j+1
            j = j+length
            decodedList.append(s[i: j+1])
            if(j+1 >= len(s)):
                break
        
        return decodedList



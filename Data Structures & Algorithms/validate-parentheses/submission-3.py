class Solution:
    def isValid(self, s: str) -> bool:
        openToCloseMap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []
        for char in s:
            if char in openToCloseMap.values():
                stack.append(char)
            elif stack and stack[-1] == openToCloseMap[char]:
                stack.pop()
            else:
                stack.append(char)
                break

        return True if not stack else False
        
        
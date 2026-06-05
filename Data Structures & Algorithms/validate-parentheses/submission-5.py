class Solution:
    def isValid(self, s: str) -> bool:
        openToCloseMap = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for char in s:
            if char not in openToCloseMap:
                stack.append(char)
            else:
                if stack and stack[-1] == openToCloseMap[char]:
                    stack.pop()
                else:
                    return False
        
        return True if len(stack) == 0 else False













        for char in s:
            if char in openToCloseMap.values():
                stack.append(char)
            elif stack and stack[-1] == openToCloseMap[char]:
                stack.pop()
            else:
                stack.append(char)
                break

        return True if not stack else False
        
        
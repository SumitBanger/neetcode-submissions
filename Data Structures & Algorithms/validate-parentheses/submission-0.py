class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracesMap = {")": "(", "}": "{", "]": "["}

        for parenthesis in s:
            if parenthesis in bracesMap:
                if stack and stack[-1] == bracesMap[parenthesis]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(parenthesis)

        return True if not stack else False
        
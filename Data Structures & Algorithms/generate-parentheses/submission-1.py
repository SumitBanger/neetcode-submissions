class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, stack = [], []

        def dfs(openCount, closeCount):
            if openCount == closeCount == n: # If we've added N open and N close braces then we've a solution
                result.append("".join(stack.copy()))
                return

            if openCount < n: # We can add 
                stack.append("(")
                dfs(openCount + 1, closeCount)
                stack.pop()
            
            if closeCount < openCount and closeCount < n:
                stack.append(")")
                dfs(openCount, closeCount + 1)
                stack.pop()

        
        dfs(0, 0)
        return result

        
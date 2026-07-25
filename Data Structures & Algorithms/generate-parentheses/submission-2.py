class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, stack = [], []

        def dfs(openCount, closeCount):
            if openCount == closeCount == n: # Added N open and N close braces then we've a solution
                result.append("".join(stack.copy()))
                return

            if openCount < n: # Add open brace only if current added open braces are less than n
                stack.append("(")
                dfs(openCount + 1, closeCount)
                stack.pop()
            
            if closeCount < openCount: # Add close brace only if current added close braces are less than open braces added
                stack.append(")")
                dfs(openCount, closeCount + 1)
                stack.pop()

        
        dfs(0, 0)
        return result

        
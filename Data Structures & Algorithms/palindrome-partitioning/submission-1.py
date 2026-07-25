class Solution:
    def partition(self, s: str) -> List[List[str]]:
        total, stack, result = len(s), [], []

        def dfs(start):
            if start >= total:
                result.append(stack.copy())
                return
            
            for end in range(start + 1, total + 1):
                subString = s[start: end]
                if self.isPalindrome(subString):
                    stack.append(subString)
                    dfs(end)
                    stack.pop()

        dfs(0)
        return result

    def isPalindrome(self, string):
        return string == string[::-1]


        
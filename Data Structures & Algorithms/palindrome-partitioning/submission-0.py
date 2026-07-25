class Solution:
    def partition(self, s: str) -> List[List[str]]:
        total, stack, result = len(s), [], []

        def dfs(start):
            if start >= total:
                result.append(stack.copy())
                return
            
            for end in range(start + 1, total + 1):
                if self.isPalindrome(s[start: end]):
                    stack.append(s[start: end])
                    dfs(end)
                    stack.pop()

        dfs(0)
        return result

    def isPalindrome(self, string):
        return string == string[::-1]


        
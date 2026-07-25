class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitTostr = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
        }

        result, stack, total = [], [], len(digits)

        def dfs(i):
            if i == total:
                result.append("".join(stack.copy()))
                return

            currentDigit = int(digits[i])
            for char in digitTostr[currentDigit]:
                stack.append(char)
                dfs(i + 1)
                stack.pop()

        if total > 0:
            dfs(0)
        return result




        
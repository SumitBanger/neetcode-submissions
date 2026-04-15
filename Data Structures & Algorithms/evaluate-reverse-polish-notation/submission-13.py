class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        temp = 0
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                first, second = stack.pop(), stack.pop()
                if token == '+':
                    temp = first + second
                elif token == '-':
                    temp = second - first
                elif token == '*':
                    temp = first * second
                elif token == '/':
                    temp = int(second / first)
                
                stack.append(int(temp))

        return stack[0]
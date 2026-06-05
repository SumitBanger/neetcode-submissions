class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators, stack = set(['+', '-', '*', '/']), []
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                second = stack.pop()
                first = stack.pop()
                if token == '+':
                    stack.append(int(first + second))
                elif token == '-':
                    stack.append(int(first - second))
                elif token == '*':
                    stack.append(int(first * second))
                else:
                    stack.append(int(first / second))
                
            print(stack)
        
        return stack[-1]

        
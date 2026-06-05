class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+" or token == "*" or token == "-" or token == "/":
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(num1 / num2)
            else:
                stack.append(int(token))
        return int(stack[-1])
        
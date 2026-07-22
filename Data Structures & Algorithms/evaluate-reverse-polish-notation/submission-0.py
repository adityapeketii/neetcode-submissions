class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ['+', '-', '*', '/']
        stack = []

        for op in tokens:
            if op not in "+-*/":
                stack.append(int(op))
            else:
                b = stack.pop()
                a = stack.pop()

                if op == "+":
                    stack.append(a+b)
                elif op == '-':
                    stack.append(a-b)
                elif op == '*':
                    stack.append(a*b)
                elif op == '/':
                    stack.append(int(a/b))
                else:
                    print("Not a Valid Operation")

        return stack[-1]        
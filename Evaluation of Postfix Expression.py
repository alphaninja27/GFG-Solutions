def evaluatePostfix(self, S):
        #code here
        s = list(S)
        stack = []
        for i in range(len(S)):
            if s[i] == '*':
                a = int(stack.pop())
                b = int(stack.pop())
                x = b * a
                stack.append(x)
            elif s[i] == '+':
                a = int(stack.pop())
                b = int(stack.pop())
                x = b + a
                stack.append(x)
            elif s[i] == '-':
                a = int(stack.pop())
                b = int(stack.pop())
                x = b - a
                stack.append(x)
            elif s[i] == '/':
                a = int(stack.pop())
                b = int(stack.pop())
                x = b // a
                stack.append(x)
            else:
                stack.append(s[i])
        return stack[0]

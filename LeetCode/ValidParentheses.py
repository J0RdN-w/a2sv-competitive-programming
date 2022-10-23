class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        top = 0
        stack.append(s[top])
        for i in s[top + 1:]:
            if top == -1:
                stack.append(i)
                top += 1
            elif stack[top] == '(' and i == ')':
                stack.pop()
                top -= 1
            elif stack[top] == '[' and i == ']':
                stack.pop()
                top -= 1
            elif stack[top] == '{' and i == '}':
                stack.pop()
                top -= 1
            else:
                stack.append(i)
                top += 1
        return len(stack) == 0
            
            

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for i in s:
            if i == ')':
                temp_stack = []
                while True:
                    e = stack.pop()
                    if e == '(':
                        break
                    temp_stack.append(e)
                stack.extend(temp_stack)
            else:
                stack.append(i)
        return ''.join(stack)
        

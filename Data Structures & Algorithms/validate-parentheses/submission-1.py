class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in list(s):
            if char == '(' or char == '[' or char == '{':
                print(char)
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    continue
                else:
                    return False
            elif char == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                    continue
                else:
                    return False
            elif char == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                    continue
                else:
                    return False
        return stack == []
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for char in list(s):
            if char in mapping.values():
                stack.append(char)
            else:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                    continue
                else:
                    return False
        return stack == []
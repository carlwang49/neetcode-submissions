class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        for char in list(s):
            if char in mapping.values():
                stack.append(char)
            else:
                if not stack or stack[-1] != mapping[char]:
                    return False
                else:
                    stack.pop()
                    
        return stack == []
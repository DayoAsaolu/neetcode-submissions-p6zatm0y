class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # ([{
        brackets = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        if len(s) % 2 != 0: return False

        i = 0
        while i < len(s):
            if s[i] not in brackets:
                stack.append(s[i])
            else:
                if not stack: return False
                curr = stack.pop()
                if brackets[s[i]] != curr:
                    return False
            i += 1

        return not stack
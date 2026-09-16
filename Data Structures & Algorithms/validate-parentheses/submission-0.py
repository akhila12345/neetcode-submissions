class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen = {'}':'{', ']':'[', ')':'('}

        for i in range(len(s)):
            if(s[i] not in closeOpen):
                stack.append(s[i])
            else:
                if stack and stack[-1] == closeOpen[s[i]]:
                    stack.pop()
                else: 
                    return False
        return True if not stack else False
            
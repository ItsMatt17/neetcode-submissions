class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "[": "]", 
            "{": "}", 
            "(": ")"
            }
        
        stack = []
        
        for c in s: 
            if c in m.keys():
                stack.append(c)
                continue
            

            if len(stack) == 0: return False
            if m[stack[-1]] != c: return False
            stack.pop()

        return len(stack) == 0
            

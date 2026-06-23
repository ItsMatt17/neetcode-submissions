class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "]": "[", 
            "}": "{", 
            ")": "("
            }
        
        stack = []
        
        for c in s: 
            if c in m.values():
                stack.append(c)
                continue
            

            if len(stack) == 0: return False
            if m[c] != stack[-1]: return False
            stack.pop()

        return len(stack) == 0
            

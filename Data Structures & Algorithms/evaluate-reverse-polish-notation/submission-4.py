class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1: return int(tokens[0])
        stack = []
    
        while tokens: 
            while tokens and (tok := tokens.pop(0)) not in ["+", "-", "*", "/"]: stack.append(int(tok)) 
            r = stack.pop()
            l = stack.pop()



            if tok == "+": l += r
            elif tok == "-": l -= r
            elif tok == "*": l *= r
            elif tok == "/": l = int(l / r)
            stack.append(l)

        return stack[0]
        

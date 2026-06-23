class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = 9 
        COLS = 9 
        GRID = 9


        for i in range(ROWS): 
            r, c, g = set(), set(), set()
            for j in range(COLS): 
                rv = board[i][j]
                cv = board[j][i]
                gv = board[(j // 3) + 3 * (i % 3)][(j % 3) + 3 * (i // 3)]
                if (rv in r) or (cv in c) or (gv in g): return False
                if rv != '.': r.add(rv)
                if cv != '.': c.add(cv)    
                if gv != '.': g.add(gv)

        return True
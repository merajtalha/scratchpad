class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [["."] * 9 for _ in range(9)]
        sqrs = [["."] * 9 for _ in range(9)]
        for i in range(9):
            seen = set()
            for j in range(9):
                elem = board[i][j]
                if elem != ".":
                    cols[j][i] = elem
                    sqrs[(i //3) * 3 + (j//3)][(i % 3) * 3 + (j % 3)] = elem
                    #check row wise
                    if elem in seen:
                        return False    #row wise fault
                    seen.add(elem)
        for i in range(9):
            seencol=set()
            seensqr=set()
            for j in range(9):
                elemcol = cols[i][j]
                elemsqr = sqrs[i][j]
                if elemcol != ".":
                    if elemcol in seencol:
                        return False
                    seencol.add(elemcol)
                if elemsqr != ".":
                    if elemsqr in seensqr:
                        return False
                    seensqr.add(elemsqr)
        return True

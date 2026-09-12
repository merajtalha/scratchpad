class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seenrow = set()
            seencol = set()
            seensqr = set()
            for j in range(9):
                elemrow = board[i][j]
                elemcol = board[j][i]
                elemsqr = board[(i //3) * 3 + (j//3)][(i % 3) * 3 + (j % 3)]
                if elemrow != ".":
                    if elemrow in seenrow:
                        return False    #row wise fault
                    seenrow.add(elemrow)
                if elemcol != ".":
                    if elemcol in seencol:
                        return False    #col wise fault
                    seencol.add(elemcol)
                if elemsqr != ".":
                    if elemsqr in seensqr:
                        return False    #sqr wise fault
                    seensqr.add(elemsqr)
        return True

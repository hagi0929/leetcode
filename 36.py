class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        Box = []
        Row = []
        Col = []
        for i in range(9):
            Box.append({})
            Row.append({})
            Col.append({})
            for j in range(1, 10):
                Box[i][j] = True
                Row[i][j] = True
                Col[i][j] = True
        for row in range(9):
            for colum in range(9):
                val = board[row][colum]
                if val != ".":
                    idxR = Row[row][int(val)]
                    idxC = Col[colum][int(val)]
                    idxB = Box[int(row / 3) * 3 + int(colum / 3)][int(val)]

                    if all([idxR, idxC, idxB]):
                        Row[row][int(val)] = False
                        Col[colum][int(val)] = False
                        Box[int(row / 3) * 3 + int(colum / 3)][int(val)] = False

                    else:
                        return False

                    print(Box)
        return True
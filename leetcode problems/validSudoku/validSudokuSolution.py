class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {
            0: "",
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        }
        cols = {
            0: "",
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        }
        box = {
            0: "",
            1: "",
            2: "",
            3: "",
            4: "",
            5: "",
            6: "",
            7: "",
            8: ""
        }
        boardBox = [[0,0,0,1,1,1,2,2,2],[3,3,3,4,4,4,5,5,5],[6,6,6,7,7,7,8,8,8]]
        boxLevel = 0
        row = 0
        col = 0
        while True:
            num = board[row][col]
            if num is not ".":
                if num in rows[row]:
                    return False
                if num in cols[col]:
                    return False
                if num in box[boardBox[boxLevel][col]]:
                    return False
                rows[row] += num
                cols[col] += num
                box[boardBox[boxLevel][col]] += num
            if col == 8 and row == 8:
                break
            elif col == 8:
                row += 1
                col = 0
                if row%3 == 0:
                    boxLevel += 1
            else:
                col += 1
        return True

class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        board2 = self.readBoard(board)
        self.solveRec(board2, 0, 0)
        self.writeBoard(board2, board)
    def solveRec(self, board, x, y):
        if x >= 9:
            x = 0
            y += 1
        if y >= 9:
            return True
        if not board[y][x] == '.':
            return self.solveRec(board, x+1, y)
        for i in range(9):
            board[y][x] = str(i + 1)
            if self.validate(board, x,y) and self.solveRec(board, x+1, y):
                return True
        board[y][x] = '.'
        return False
            
    def validate(self, board, x, y):
        self.board = board
        return self.checkRow(y) and self.checkColumn(x) and self.checkBox(x, y)
    
    def checkRow(self, y):
        seen = set()
        for btn in self.board[y]:
            num = btn
            if num in seen and not num == '.':
                return False
            seen.add(num)
        return True
    
    def checkColumn(self, x):
        seen = set()
        for i in range(9):
            num = self.board[i][x]
            if num in seen and not num == '.':
                return False
            seen.add(num)
        return True
    
    def checkBox(self, x, y):
        x -= x%3
        y -= y%3
        seen = set()
        for i in range(x, x + 3):
            for j in range(y, y + 3):
                num = self.board[i][j]
                if num in seen and not num == '.':
                    return False
                seen.add(num)     
        return True

    def writeBoard(self, board, buttonListing):
        for i in range(len(board)):
            for j in range(len(buttonListing)):
                buttonListing[i][j]["text"] = board[i][j]
    
    def readBoard(self, board):
        board2 = []
        for i in range(len(board)):
            board2.append([])
            for j in range(len(board)):
                board2[i].append(board[i][j]["text"])
        return board2

if __name__ == '__main__':
    soln = Solution()
    sample = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    soln.solveRec(sample, 0, 0)
    supposed = [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]

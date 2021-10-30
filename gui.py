import tkinter as tk
from coreAlgo import Solution
WIDTH, LENGTH = 9,9

def square_draw(col, row):
    bt = tk.Button(window, width=4, height=2, text=".", command=lambda: click(col, row))
    bt.grid(column=(col+1)*2, row=(row+1)*2)
    return bt

def click(col, row):
    curr = listing[col][row]
    if curr["text"] == ".":
        curr["text"] = "1"
    elif curr["text"] == "9":
        curr["text"] = "."
    else:
        curr["text"] = str(int(curr["text"]) + 1)
    
window = tk.Tk()
window.title("Sudoku Solver")

disp = tk.Label(window, text="Sudoku Solver")
disp.grid(column=0, row=0, columnspan=WIDTH*5)
listing = []
for i in range(WIDTH):
    listing.append([])
    for j in range(LENGTH):
        listing[i].append(square_draw(i,j))

soln = Solution()
sample = board2 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
soln.writeBoard(sample, listing)
bt = tk.Button(window, width=4, height=2, text="Solve", command=lambda:soln.solveSudoku(listing))
bt.grid(column = 4*2, row=10*2)
window.mainloop()
import tkinter as tk
from tkinter import messagebox

class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.user_inputs = [[False for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_solve_button()

    def create_grid(self):
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(self.root, width=2, font=('Arial', 18), justify='center', bd=2, relief='ridge', fg='black')
                entry.grid(row=row, column=col, padx=1, pady=1)
                self.entries[row][col] = entry

    def create_solve_button(self):
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku, font=('Arial', 14), bg='lightblue')
        solve_button.grid(row=9, column=0, columnspan=9, sticky="nsew", pady=10)

    def get_board(self):
        board = []
        for row in range(9):
            current_row = []
            for col in range(9):
                val = self.entries[row][col].get()
                if val.isdigit() and 1 <= int(val) <= 9:
                    current_row.append(int(val))
                    self.user_inputs[row][col] = True
                else:
                    current_row.append(0)
                    self.user_inputs[row][col] = False
            board.append(current_row)
        return board

    def fill_board(self, board):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].insert(0, str(board[row][col]))
                if self.user_inputs[row][col]:
                    self.entries[row][col].config(fg='black')  # User input
                else:
                    self.entries[row][col].config(fg='blue')   # Solver-filled

    def is_valid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(board, row, col, num):
                            board[row][col] = num
                            if self.solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def solve_sudoku(self):
        board = self.get_board()
        if self.solve(board):
            self.fill_board(board)
        else:
            messagebox.showerror("No solution", "This Sudoku puzzle cannot be solved.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()

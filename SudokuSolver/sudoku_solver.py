import tkinter as tk
from tkinter import messagebox


class SudokuSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.user_inputs = [[False for _ in range(9)] for _ in range(9)]
        self.create_grid()
        self.create_buttons()

    def create_grid(self):
        self.root.configure(bg='black')
        for row in range(9):
            for col in range(9):
                entry = tk.Entry(
                    self.root, width=2, font=('Arial', 18), justify='center',
                    bd=2, relief='ridge', fg='white', bg='black', insertbackground='white'
                )
                entry.grid(row=row, column=col, padx=1, pady=1)
                self.entries[row][col] = entry

    def create_buttons(self):
        # Solve button in middle row, spanning all columns
        solve_button = tk.Button(self.root, text="Solve", command=self.solve_sudoku,
                                 font=('Arial', 14), bg='lightblue')
        solve_button.grid(row=9, column=0, columnspan=9, sticky="nsew", pady=10, padx=5)

        # Bottom row buttons: Use Sample Test Case and Reset
        load_button = tk.Button(self.root, text="Use Sample Test Case", command=self.load_test_case,
                                font=('Arial', 14), bg='lightgreen')
        load_button.grid(row=10, column=0, columnspan=5, sticky="nsew", pady=(0, 10), padx=(5, 2))

        reset_button = tk.Button(self.root, text="Reset", command=self.reset_board,
                                 font=('Arial', 14), bg='lightgray')
        reset_button.grid(row=10, column=5, columnspan=4, sticky="nsew", pady=(0, 10), padx=(2, 5))

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
                    self.entries[row][col].config(fg='white')
                else:
                    self.entries[row][col].config(fg='lime')

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

    def load_test_case(self):
        test_case = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                if test_case[row][col] != 0:
                    self.entries[row][col].insert(0, str(test_case[row][col]))
                self.user_inputs[row][col] = (test_case[row][col] != 0)
                self.entries[row][col].config(fg='white')

    def reset_board(self):
        for row in range(9):
            for col in range(9):
                self.entries[row][col].delete(0, tk.END)
                self.entries[row][col].config(fg='white')


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuSolverGUI(root)
    root.mainloop()

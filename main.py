import tkinter as tk
import random
from tkinter import messagebox

class Mineursweeper:
    def __init__(self, master, grid_size=30, mines=30):
        self.master = master
        self.grid_size = grid_size
        self.mines = mines
        self.limit = 0
        self.buttons = [[None for _ in range(grid_size)] for _ in range(grid_size)]
        self.is_mine = [[False for _ in range(grid_size)] for _ in range(grid_size)]
        self.is_revealed = [[False for _ in range(grid_size)] for _ in range(grid_size)]  # To track revealed cells
        self.initialize_game()

    def initialize_game(self):
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                btn = tk.Button(self.master, width=2, height=1,
                                command=lambda x=x, y=y: self.cell_click(x, y))
                btn.grid(row=x, column=y)
                self.buttons[x][y] = btn

        # Place mines
        mines_placed = 0
        while mines_placed < self.mines:
            x, y = random.randint(0, self.grid_size-1), random.randint(0, self.grid_size-1)
            if not self.is_mine[x][y]:
                self.is_mine[x][y] = True
                mines_placed += 1

    def cell_click(self, x, y):
        if self.is_mine[x][y]:
            messagebox.showinfo("Game Over", "You clicked on a mine!")
            self.master.destroy()  # or reset game
        else:
            self.reveal_cell(x, y)

    def reveal_cell(self, x, y, limit=0):
        if self.is_revealed[x][y] or limit > 9:  # If cell is already revealed, do nothing
            return
        self.is_revealed[x][y] = True
        adjacent_mines = self.count_adjacent_mines(x, y)
        if adjacent_mines > 0:
            self.buttons[x][y].config(text=str(adjacent_mines), relief=tk.SUNKEN, state=tk.DISABLED)
        else:
            self.buttons[x][y].config(relief=tk.SUNKEN, state=tk.DISABLED)
            # Recursively reveal neighboring cells if there are no adjacent mines
            for i in range(max(0, x-1), min(x+2, self.grid_size)):
                for j in range(max(0, y-1), min(y+2, self.grid_size)):
                    if not self.is_mine[i][j]:
                        self.reveal_cell(i, j, limit+1)

    def count_adjacent_mines(self, x, y):
        count = 0
        for i in range(max(0, x-1), min(x+2, self.grid_size)):
            for j in range(max(0, y-1), min(y+2, self.grid_size)):
                if self.is_mine[i][j]:
                    count += 1
        return count

def main():
    root = tk.Tk()
    root.title("Elle est super mature en vrai")
    game = Mineursweeper(root)
    root.mainloop()

if __name__ == "__main__":
    main()

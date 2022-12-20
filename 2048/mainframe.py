from tkinter import *
import enums as e
import numpy as np
import random


class Game(Frame):
    # UI Part
    def __init__(self):
        Frame.__init__(self)
        self.master.title("2048 THE Game")
        self.master.geometry("{}x{}".format(e.WINDOW_SIZE, e.WINDOW_SIZE))
        self.grid()

        self.board = []
        self.states = []
        self.matrix = []

        self.start_game()
        self.init_grid()

        self.master.bind("<Key>", self.move)
        self.states.append(self.matrix)

        self.mainloop()

    def init_grid(self):
        # creating main containers
        background = Frame(self, bg=e.BACKGROUND, width=e.WINDOW_SIZE, height=e.WINDOW_SIZE)

        # layout
        background.grid_rowconfigure(0, weight=1)
        background.grid_columnconfigure(1, weight=1)
        background.place(in_=self, anchor=CENTER, relx=0.5, rely=0.5)
        background.grid()
        # TBD CENTER

        for i in range(e.SIZE):
            grid_row = []
            for j in range(e.SIZE):
                cell = Frame(background, bg=e.BG_CELL, width=e.CELL_WIDTH, height=e.CELL_HEIGHT)
                cell.grid(row=i, column=j, padx=10, pady=10)
                t = Label(master=cell, text=str(self.matrix[i][j]), bg=e.BG_CELL, justify=CENTER, width=5, height=2)
                t.grid()
                grid_row.append(t)
            self.board.append(grid_row)

    def update_grid(self):
        print(self.board)
        for i in range(e.SIZE):
            for j in range(e.SIZE):
                new_value = self.matrix[i][j]
                if new_value == 0:
                    self.board[i][j].configure(text="0", bg=e.BG_CELL, fg=e.FG_CELL)
                else:
                    self.board[i][j].configure(text=str(new_value), bg=e.BG_CELL, fg=e.FG_CELL)
        self.update_idletasks()

    def start_game(self):
        no_values = random.randint(2, 6)
        self.matrix = np.zeros((e.SIZE, e.SIZE), dtype=int)
        for i in range(no_values):
            self.add_random_two()

    # Functions
    def add_random_two(self):
        row = random.randint(0, e.SIZE - 1)
        col = random.randint(0, e.SIZE - 1)
        while self.matrix[col][row] != 0:
            row = random.randint(0, e.SIZE - 1)
            col = random.randint(0, e.SIZE - 1)
        self.matrix[row][col] = 2

    def compress(self):
        new_matrix = np.zeros((4, 4), dtype=int)
        for i in range(e.SIZE):
            position = 0
            for j in range(e.SIZE):
                if self.matrix[i][j] != 0:
                    new_matrix[i][position] = self.matrix[i][j]
                    position += 1
        self.matrix = new_matrix

    def combine(self):
        for i in range(e.SIZE):
            for j in range(e.SIZE - 1):
                if self.matrix[i][j] != 0:
                    if self.matrix[i][j] == self.matrix[i][j + 1]:
                        self.matrix[i][j] *= 2
                        self.matrix[i][j + 1] = 0

    def gather_and_stack(self):
        self.compress()
        self.combine()
        self.compress()
        return True

    def reverse(self):
        self.matrix = np.fliplr(self.matrix)

    def transpose(self):
        self.matrix = np.transpose(self.matrix)

    def move(self, event):
        key = event.keysym
        print(event)
        print(key)

        if key == e.KEY_RESET:
            self.start_game()

        if key == e.KEY_UP:
            self.transpose()
            done = self.gather_and_stack()
            self.transpose()
            print(self.matrix)

        elif key == e.KEY_DOWN:
            self.transpose()
            self.reverse()
            done = self.gather_and_stack()
            self.reverse()
            self.transpose()
            print(self.matrix)

        elif key == e.KEY_LEFT:
            done = self.gather_and_stack()
            print(self.matrix)

        elif key == e.KEY_RIGHT:
            self.reverse()
            done = self.gather_and_stack()
            self.reverse()
            print(self.matrix)

        if done:
            self.add_random_two()
            self.update_grid()
            self.states.append(self.matrix)


if __name__ == '__main__':
    game = Game()

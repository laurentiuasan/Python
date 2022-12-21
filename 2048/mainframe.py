from tkinter import *
import enums as e
import numpy as np
import random
import time


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

        self.master.bind("<Key>", self.pressed_key)
        self.states.append(self.matrix)

        self.mainloop()

    def init_grid(self):
        # creating main containers
        background = Frame(self, bg=e.BACKGROUND, width=e.WINDOW_SIZE, height=e.WINDOW_SIZE)

        # layout
        background.grid_rowconfigure(0, weight=1)
        background.grid_columnconfigure(1, weight=1)
        background.grid()
        # TBD CENTER

        for i in range(e.SIZE):
            grid_row = []
            for j in range(e.SIZE):
                cell = Frame(background, bg=e.CELLS_BG[2], width=e.CELL_WIDTH, height=e.CELL_HEIGHT)
                cell.grid(row=i, column=j, padx=10, pady=10)
                if self.matrix[i][j] == 0:
                    t = Label(master=cell, text="", bg=e.CELLS_BG[self.matrix[i][j]],
                              justify=CENTER, width=10, height=4)
                else:
                    t = Label(master=cell, text=str(self.matrix[i][j]), bg=e.CELLS_BG[2], fg=e.CELLS_FG[2],
                              justify=CENTER, width=10, height=4)
                t.grid()
                grid_row.append(t)
            self.board.append(grid_row)

    def update_grid(self):
        print(self.board)
        for i in range(e.SIZE):
            for j in range(e.SIZE):
                new_value = self.matrix[i][j]
                if new_value == 0:
                    self.board[i][j].configure(text="", bg=e.CELLS_BG[new_value])
                else:
                    self.board[i][j].configure(text=str(new_value), bg=e.CELLS_BG[new_value], fg=e.CELLS_FG[new_value])
        self.update_idletasks()

    def start_game(self):
        no_values = random.randint(2, 6)
        self.matrix = np.zeros((e.SIZE, e.SIZE), dtype=int)
        for i in range(no_values):
            self.add_random_two()

    # Functions
    def add_random_two(self):
        free_cells = np.argwhere(self.matrix == 0)
        random_index1 = np.random.randint(0, e.SIZE - 1)
        random_index2 = np.random.randint(0, e.SIZE - 1)
        self.matrix[random_index1][random_index2] = random.choice([2, 4])

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

    def reverse(self):
        self.matrix = np.fliplr(self.matrix)

    def transpose(self):
        self.matrix = np.transpose(self.matrix)

    def pressed_key(self, event):
        key = event.keysym
        print(event)
        print(key)

        if key == e.KEY_RESET:
            self.start_game()
            print(self.states)
            self.states = []

        if key == e.KEY_UP:
            self.transpose()
            self.gather_and_stack()
            time.sleep(0.1)
            self.transpose()
            print(self.matrix)

        elif key == e.KEY_DOWN:
            self.transpose()
            self.reverse()
            self.gather_and_stack()
            time.sleep(0.1)
            self.reverse()
            self.transpose()
            print(self.matrix)

        elif key == e.KEY_LEFT:
            self.gather_and_stack()
            time.sleep(0.1)
            print(self.matrix)

        elif key == e.KEY_RIGHT:
            self.reverse()
            self.gather_and_stack()
            time.sleep(0.1)
            self.reverse()
            print(self.matrix)

        self.add_random_two()
        self.update_grid()
        self.states.append(self.matrix)


if __name__ == '__main__':
    game = Game()

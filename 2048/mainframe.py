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
        self.game_over = False

        # creating main containers
        self.background = Frame(self, bg=e.BACKGROUND, width=e.WINDOW_SIZE, height=e.WINDOW_SIZE)

        self.start_game()
        self.gui_grid()

        self.master.bind("<Key>", self.pressed_key)
        self.states.append(self.matrix)

        self.mainloop()

    def gui_grid(self):

        # layout
        self.background.grid_rowconfigure(0, weight=1)
        self.background.grid_columnconfigure(1, weight=1)
        self.background.pack(side="bottom", padx=50, pady=50)
        self.background.grid()
        # TBD CENTER

        for i in range(e.SIZE):
            grid_row = []
            for j in range(e.SIZE):
                cell = Frame(self.background, bg=e.CELLS_BG[2], width=e.CELL_WIDTH, height=e.CELL_HEIGHT)
                cell.grid(row=i, column=j, padx=10, pady=10)
                if self.matrix[i][j] == 0:
                    cell_containing = Label(master=cell, text="", bg=e.CELLS_BG[self.matrix[i][j]],
                                            justify=CENTER, width=10, height=4)
                else:
                    cell_containing = Label(master=cell, text=str(self.matrix[i][j]), bg=e.CELLS_BG[2],
                                            fg=e.CELLS_FG[2], justify=CENTER, width=10, height=4)
                cell_containing.grid()
                grid_row.append(cell_containing)
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

    # Functions
    def start_game(self):
        self.game_over = False
        no_values = random.randint(2, 6)
        self.matrix = np.zeros((e.SIZE, e.SIZE), dtype=int)
        for i in range(no_values):
            self.add_random_two()

    def add_random_two(self):
        free_cells = np.argwhere(self.matrix == 0)
        random_row = np.random.choice(len(free_cells), size=1, replace=False)
        chosen_one = free_cells[random_row, :]
        row = chosen_one[0][0]
        col = chosen_one[0][1]
        print(row, col)
        self.matrix[row, col] = random.choice([2, 4])

    def check_game_state(self):
        # checks if you won and display a text
        if any(2048 in row for row in self.matrix):
            end_game_frame = Frame(self.background, name="game_won")
            end_game_frame.place(relx=0.5, rely=0.5, anchor="center")
            win_text = Label(end_game_frame, text="YOU WON!", bg=e.WIN_BG)
            win_text.pack()
            self.game_over = True

        # checks if you lost
        if not any(0 in row for row in self.matrix):
            horizontal, vertical = False, False
            for i in range(e.SIZE):
                for j in range(e.SIZE - 1):
                    if self.matrix[i][j] == self.matrix[i][j + 1]:
                        horizontal = True
            for i in range(e.SIZE - 1):
                for j in range(e.SIZE):
                    if self.matrix[i][j] == self.matrix[i + 1][j]:
                        vertical = True
            # display a text saying that you lost
            if not horizontal and not vertical:
                end_game_frame = Frame(self.background, name="game_lost")
                end_game_frame.place(relx=0.5, rely=0.5, anchor="center")
                lose_text = Label(end_game_frame, text="GAME OVER!", bg=e.LOST_BG)
                lose_text.pack()
                self.game_over = True

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
                        self.matrix[i][j] *= 8
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
            for widget in self.background.winfo_children():
                if widget.winfo_name() in ["game_won", "game_lost"]:
                    widget.destroy()

            print(self.states)
            self.start_game()
            self.states = []

        if not self.game_over:
            if key == e.KEY_UP:
                self.transpose()
                self.gather_and_stack()
                time.sleep(0.1)
                self.transpose()

            elif key == e.KEY_DOWN:
                self.transpose()
                self.reverse()
                self.gather_and_stack()
                time.sleep(0.1)
                self.reverse()
                self.transpose()

            elif key == e.KEY_LEFT:
                self.gather_and_stack()
                time.sleep(0.1)

            elif key == e.KEY_RIGHT:
                self.reverse()
                self.gather_and_stack()
                time.sleep(0.1)
                self.reverse()

            print(self.matrix)
            self.add_random_two()
            self.check_game_state()
            self.update_grid()
            self.states.append(self.matrix)


if __name__ == '__main__':
    game = Game()

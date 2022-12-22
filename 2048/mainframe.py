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
        self.score = 0
        self.done = False

        # creating main containers
        self.background = Frame(self, bg=e.BACKGROUND, width=e.WINDOW_SIZE, height=e.WINDOW_SIZE)

        self.start_game()
        self.gui_grid()

        self.master.bind("<Key>", self.pressed_key)

        self.mainloop()

    def gui_grid(self):

        # layout
        self.background.grid_rowconfigure(0, weight=1)
        self.background.grid_columnconfigure(1, weight=1)
        self.background.pack(side="bottom", padx=50, pady=50)
        self.background.grid()

        # grids
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

    # updating ui
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

    # initiate matrix
    def start_game(self):
        self.game_over = False
        no_values = random.randint(2, 4)
        self.matrix = np.zeros((e.SIZE, e.SIZE), dtype=int)
        for i in range(no_values):
            self.add_random_two()
        self.score = 0
        self.states.append((self.matrix, "0", self.score))
        print(self.matrix)

    # generate random tile
    def add_random_two(self):
        free_cells = np.argwhere(self.matrix == 0)
        random_row = np.random.choice(len(free_cells), size=1, replace=False)
        chosen_one = free_cells[random_row, :]
        row = chosen_one[0][0]
        col = chosen_one[0][1]
        print(row, col)
        self.matrix[row, col] = random.choice([2, 4])

    # checks if there is any horizontal moves available
    def horizontal_moves(self):
        for i in range(e.SIZE):
            for j in range(e.SIZE - 1):
                if self.matrix[i][j] == self.matrix[i][j + 1] or self.matrix[i][j] == 0 or self.matrix[i][j + 1] == 0:
                    return True
        return False

    # checks if there is any vertically moves available
    def vertical_moves(self):
        for i in range(e.SIZE - 1):
            for j in range(e.SIZE):
                if self.matrix[i][j] == self.matrix[i + 1][j] or self.matrix[i][j] == 0 or self.matrix[i][j + 1] == 0:
                    return True
        return False

    # checks weather you won or lost
    def check_game_state(self):
        # checks if you won and display a text
        if any(2048 in row for row in self.matrix):
            end_game_frame = Frame(self.background, name="game_won")
            end_game_frame.place(relx=0.5, rely=0.5, anchor="center")
            win_text = Label(end_game_frame, text="YOU WON! Your score is: {}".format(self.score), bg=e.WIN_BG)
            win_text.pack()
            self.game_over = True

        # checks if you lost
        if not any(0 in row for row in self.matrix):
            horizontal, vertical = self.horizontal_moves(), self.vertical_moves()
            # display a text saying that you lost
            if not horizontal and not vertical:
                end_game_frame = Frame(self.background, name="game_lost")
                end_game_frame.place(relx=0.5, rely=0.5, anchor="center")
                lose_text = Label(end_game_frame, text="GAME OVER! Your score is: {}".format(self.score), bg=e.LOST_BG)
                lose_text.pack()
                self.game_over = True

    # pulls all the tiles together
    def compress(self):
        new_matrix = np.zeros((4, 4), dtype=int)
        for i in range(e.SIZE):
            position = 0
            for j in range(e.SIZE):
                if self.matrix[i][j] != 0:
                    new_matrix[i][position] = self.matrix[i][j]
                    position += 1
        self.matrix = new_matrix

    # stacks any 2 adjacent tiles with the same value
    def combine(self):
        for i in range(e.SIZE):
            for j in range(e.SIZE - 1):
                if self.matrix[i][j] != 0:
                    if self.matrix[i][j] == self.matrix[i][j + 1]:
                        self.matrix[i][j] *= 2
                        self.matrix[i][j + 1] = 0
                        self.score += self.matrix[i][j]

    # shortcut for our 2 repeated functions
    def gather_and_stack(self):
        self.compress()
        self.combine()
        self.compress()

    # reverse the matrix
    def reverse(self):
        self.matrix = np.fliplr(self.matrix)

    # transpose
    def transpose(self):
        self.matrix = np.transpose(self.matrix)

    # checks for any key pressed and does the action
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

        if key == e.KEY_BACK:
            if len(self.states) > 1:
                self.states.pop()
                self.matrix = self.states[-1][0]
                self.score = self.states[-1][2]
                self.game_over = False
                for widget in self.background.winfo_children():
                    if widget.winfo_name() in ["game_won", "game_lost"]:
                        widget.destroy()
                self.update_grid()

        if not self.game_over:
            exists_vertically_moves = self.vertical_moves()
            exists_horizontally_moves = self.horizontal_moves()
            if exists_vertically_moves:
                if key == e.KEY_UP:
                    self.transpose()
                    self.gather_and_stack()
                    time.sleep(0.1)
                    self.transpose()
                    self.done = True

                elif key == e.KEY_DOWN:
                    self.transpose()
                    self.reverse()
                    self.gather_and_stack()
                    time.sleep(0.1)
                    self.reverse()
                    self.transpose()
                    self.done = True

            if exists_horizontally_moves:
                if key == e.KEY_LEFT:
                    self.gather_and_stack()
                    time.sleep(0.1)
                    self.done = True

                elif key == e.KEY_RIGHT:
                    self.reverse()
                    self.gather_and_stack()
                    time.sleep(0.1)
                    self.reverse()
                    self.done = True

            if key != "BackSpace":
                if len(np.argwhere(self.matrix == 0)) != 0 and self.done:
                    time.sleep(0.2)
                    self.add_random_two()
                    self.done = False
                self.check_game_state()
                self.states.append((self.matrix, key, self.score))
            self.update_grid()
            print(self.states)
            print(self.matrix)


if __name__ == '__main__':
    game = Game()

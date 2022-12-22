import tkinter.messagebox
from tkinter import *
import enums as e
import functions as f
import numpy as np
import random
import time
import sys

"""
    Cerinte:
 1. Auto-adaptarea marimii ferestrei
 2. dupa terminarea jocului, poti alege sa continui sau nu (UI+cod)
 3. un AI pentru un mod de joc mai greu/haotic
 
 Adaptarea ferestrei s-a facut comentand o linie de cod;
 Am adaugat un messagebox pentru continuare in cazul de castig
 Pentru rularea AI-ului ce genereaza haotic tile-uri se da valoarea 1 la linia de comanda, iar 0 pentru random placement
 """


class Game(Frame):
    # UI Part
    def __init__(self, mode):
        Frame.__init__(self)
        self.master.title("2048 THE Game")
        # self.master.geometry("{}x{}".format(e.WINDOW_SIZE, e.WINDOW_SIZE))
        self.grid()

        self.board = []
        self.states = []
        self.matrix = []
        self.game_over = False
        self.score = 0
        self.continue_game = False  # in order to continue without checking win/lose conditions
        self.mode = mode
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
        for i in range(e.SIZE):
            for j in range(e.SIZE):
                new_value = self.matrix[i][j]
                if new_value == 0:
                    self.board[i][j].configure(text="", bg=e.CELLS_BG[new_value])
                elif new_value <= 2048:
                    self.board[i][j].configure(text=str(new_value), bg=e.CELLS_BG[new_value], fg=e.CELLS_FG[new_value])
                else:   # same color for everything over 4096
                    self.board[i][j].configure(text=str(new_value), bg=e.CELLS_BG[4096], fg=e.CELLS_FG[4096])
        self.update_idletasks()

    # initiate matrix
    def start_game(self):
        self.game_over = False
        no_values = random.randint(2, 4)
        self.matrix = np.zeros((e.SIZE, e.SIZE), dtype=int)
        for i in range(no_values):
            self.generate_tile(0)
        self.score = 0
        self.continue_game = False
        self.states.append((self.matrix, "0", self.score))

    def ai_adds_tiles(self):
        # Evaluate
        moves = ["w", "s", "a", "d"]
        best_score = -1
        best_moves = []
        for i in range(4):
            temp = self.matrix[:][:]
            moved_temp, _, _ = f.move(moves[i], temp, self.score)
            score = f.calculate_score(moved_temp)
            print(f"Score is {score}")
            if score > best_score:
                best_score = score
                if len(best_moves):
                    best_moves.pop()
                best_moves.append(moves[i])
            elif score == best_score:
                best_moves.append(moves[i])
        print(f"Best moves are: {best_moves}")

        # Generate tile to block the best move
        values = [self.matrix[i][j] for i in range(e.SIZE) for j in range(e.SIZE)]
        sorted_values = np.unique(values)
        sorted_values = np.flip(sorted_values)
        chosen = ()
        unfit = False

        for i in sorted_values:
            pos_max = np.where(values == i)
            for pos in range(len(pos_max)):
                for j in best_moves:
                    if (j == "w" or unfit) and (pos_max[pos][0] - 4) > 0:
                        if values[pos_max[pos][0] - 4] == 0:
                            chosen = (int((pos_max[pos][0] - 4) / 4), int((pos_max[pos][0] - 4) % 4))

                    elif (j == "s" or unfit) and (pos_max[pos][0] + 4) < 16:
                        if values[pos_max[pos][0] - 4] == 0:
                            chosen = (int((pos_max[pos][0] + 4) / 4), int((pos_max[pos][0] + 4) % 4))

                    elif (j == "a" or unfit) and (pos_max[pos][0] - 1) > 0 and (pos_max[pos][0] % 4 != 0):
                        if values[(pos_max[pos][0] - 1)] == 0:
                            chosen = (int((pos_max[pos][0] - 1) / 4), int((pos_max[pos][0] - 1) % 4))

                    elif (j == "d" or unfit) and (pos_max[pos][0] + 1) < 16 and (pos_max[pos][0] % 4 != 3):
                        if values[pos_max[pos][0] + 1] == 0:
                            chosen = (int((pos_max[pos][0] + 1) / 4), int((pos_max[pos][0] + 1) % 4))
                if chosen:
                    break
            if pos == len(pos_max) - 1:
                unfit = True
            if chosen:
                if self.matrix[chosen[0]][chosen[1]] == 0 and 0 <= chosen[0] <= 3 and 0 <= chosen[1] <= 3:
                    unfit = False
                    break
        self.matrix[chosen[0]][chosen[1]] = np.random.choice([2, 4, 8], p=[0.8, 0.15, 0.05])

    # generate tiles given mode(0 = random, 1 = ai chaotic)
    def generate_tile(self, mode):
        if mode == 1:
            self.ai_adds_tiles()
        else:
            free_cells = np.argwhere(self.matrix == 0)
            random_row = np.random.choice(len(free_cells), size=1, replace=False)
            chosen_one = free_cells[random_row, :]
            row = chosen_one[0][0]
            col = chosen_one[0][1]
            self.matrix[row, col] = random.choice([2, 4])

    # deletes additional ui from win/lost screen
    def delete_endgame_ui(self):
        for widget in self.background.winfo_children():
            if widget.winfo_name() in ["game_won", "game_lost", "yes_button", "no_button"]:
                widget.destroy()

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
                if self.matrix[i][j] == self.matrix[i + 1][j] or self.matrix[i][j] == 0 or self.matrix[i + 1][j] == 0:
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

            continue_question = tkinter.messagebox.askyesno(title="continue", message="Do you want to continue?")
            if continue_question:
                self.continue_game = True
                self.game_over = False
                self.delete_endgame_ui()
            else:
                self.continue_game = False
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

                reset_question = tkinter.messagebox.askyesno(title="reset", message="Do you want to restart the game?")
                if reset_question:
                    self.delete_endgame_ui()
                    self.states = []
                    self.start_game()
                    self.game_over = False
                else:
                    self.game_over = True

    # checks for any key pressed and does the action
    def pressed_key(self, event):
        key = event.keysym
        print(event)
        print(key)

        if key == e.KEY_RESET:
            self.delete_endgame_ui()
            print(self.states)
            self.states = []
            self.start_game()

        if key == e.KEY_BACK:
            if len(self.states) > 1:
                self.states.pop()
                self.matrix = self.states[-1][0]
                self.score = self.states[-1][2]
                self.game_over = False
                self.continue_game = False
                self.delete_endgame_ui()
                self.update_grid()

        if not self.game_over:
            exists_vertically_moves = self.vertical_moves()
            exists_horizontally_moves = self.horizontal_moves()
            if exists_vertically_moves:
                if key == e.KEY_UP:
                    self.matrix, self.score, self.done = f.move_up(self.matrix, self.score)

                elif key == e.KEY_DOWN:
                    self.matrix, self.score, self.done = f.move_down(self.matrix, self.score)

            if exists_horizontally_moves:
                if key == e.KEY_LEFT:
                    self.matrix, self.score, self.done = f.move_left(self.matrix, self.score)

                elif key == e.KEY_RIGHT:
                    self.matrix, self.score, self.done = f.move_right(self.matrix, self.score)

            if key != "BackSpace":
                if len(np.argwhere(self.matrix == 0)) != 0 and self.done:
                    time.sleep(0.2)
                    self.generate_tile(self.mode)
                    self.done = False

                if not self.continue_game:
                    self.update_grid()
                    self.check_game_state()
                    self.update_grid()
                else:
                    self.update_grid()

                if key != "r":
                    self.states.append((self.matrix, key, self.score))

            print(self.states)


if __name__ == '__main__':
    game_mode = int(sys.argv[1])
    game = Game(game_mode)

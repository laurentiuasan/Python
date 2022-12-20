from tkinter import *
import enums as e
import numpy as np
import functions


class Game(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.master.title("2048 THE Game")
        self.master.geometry("{}x{}".format(e.WINDOW_SIZE, e.WINDOW_SIZE))
        self.master.bind("<Key>", self.pressed_key)
        self.grid()

        self.board = []
        self.states = []
        self.matrix = functions.init_game()

        self.init_grid()

        self.commands = {
            e.KEY_UP: functions.move(self.matrix, "up"),
            e.KEY_DOWN: functions.move(self.matrix, "down"),
            e.KEY_LEFT: functions.move(self.matrix, "left"),
            e.KEY_RIGHT: functions.move(self.matrix, "right"),
            e.KEY_RESET: functions.init_game()
        }

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

    def pressed_key(self, event):
        key = event.keysym
        print(event)
        if key in self.commands:
            self.matrix = self.commands[key]
            self.update_grid()
            self.states.append(self.matrix)


if __name__ == '__main__':
    game = Game()

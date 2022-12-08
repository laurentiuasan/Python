from tkinter import *
import enums as e
import numpy as np


class Game():
    def __init__(self):
        self.board = []
        self.matrix = np.zeros((4, 4), dtype=int)
        self.states = []
        self.init_grid()

    def init_grid(self):
        root = Tk()
        root.geometry("{}x{}".format(e.WIDTH, e.HEIGHT))
        root.title("2048 THE Game")

        # creating main containers
        top_frame = Frame(root, bg=e.BACKGROUND, width=e.WIDTH, height=e.HEIGHT / 10, pady=20)
        bottom_frame = Frame(root, bg=e.BACKGROUND, width=e.WIDTH, height=e.HEIGHT - e.HEIGHT / 10)

        # layout
        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)
        top_frame.grid(row=0, sticky=e.LEFT_TO_RIGHT)
        bottom_frame.grid(row=1, sticky=e.CENTERED)

        # creating widgets for bottom frame
        bottom_frame.grid_rowconfigure(0, weight=1)
        bottom_frame.grid_columnconfigure(1, weight=1)

        bottom_center = Frame(bottom_frame, bg=e.BG_BOTTOM_CENTER_FRAME, width=250, height=250)

        bottom_center.place(relx=0.5, rely=0.5, anchor=CENTER)

        for i in range(4):
            grid_row = []
            for j in range(4):
                cell = Frame(bottom_center, bg=e.BG_CELL, width=e.CELL_WIDTH, height=e.CELL_HEIGHT)
                cell.grid(row=i, column=j, padx=10, pady=10)
                t = Label(master=cell, text=str(self.matrix[i][j]), bg=e.BG_CELL, justify=CENTER, width=5, height=2)
                t.grid()
                grid_row.append(t)
            self.board.append(grid_row)

        root.mainloop()


if __name__ == '__main__':
    game = Game()


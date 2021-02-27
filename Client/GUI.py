import tkinter as tk
from functools import *

BLACK = '⚫'
BLACK_KING = '■'
WHITE = '◯'
WHITE_KING = '□'
EMPTY = ' '


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.resizable(0, 0)
        self.desk = [[EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK],
                     [BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY],
                     [EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK],
                     [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                     [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
                     [WHITE, EMPTY, WHITE, EMPTY, WHITE, EMPTY, WHITE, EMPTY],
                     [EMPTY, WHITE, EMPTY, WHITE, EMPTY, WHITE, EMPTY, WHITE],
                     [WHITE, EMPTY, WHITE, EMPTY, WHITE, EMPTY, WHITE, EMPTY]]
        self.buttons = []
        self.commands = []
        self.tap_button = ' '
        for y in range(len(self.desk)):
            for x in range(len(self.desk)):
                button = tk.Button(self, text=self.desk[y][x],
                                   command=partial(self.listen_button, x, y))
                self.buttons.append(button)
                button.grid(row=y, column=x, sticky='nswe')

    def put_checker(self, x, y, checker):
        self.buttons[y * 8 + x].configure(text=checker)

    def listen_button(self, x, y):
        self.tap_button = (x, y)
        print(self.tap_button)

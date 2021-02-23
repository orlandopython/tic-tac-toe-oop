"""
Tic Tac Toe

This uses Turtle graphics to draw the game board
It puts some "self protection" in the button class
"""

import sys
from turtle import Screen, Turtle
from typing import Callable

FONT = ("Arial", 24, "bold")
BUTTON_COLOR = "blue"
SYMBOL_COLOR = "white"
BUTTON_STRETCH = 5
BUTTON_SHAPE = "square"
FILLER = " "
XOFFSET, YOFFSET = -200, 200  # normally starts in center of window, yuck


class Button(Turtle):
    def __init__(self, row: int, column: int):
        super().__init__(visible=False)
        self.penup()
        self.hideturtle()
        self.color(BUTTON_COLOR)
        self.pencolor(SYMBOL_COLOR)
        self.id = (row, column)  # not actually used but good if you want it smarter
        self.shape(BUTTON_SHAPE)
        self.setposition(x=XOFFSET + column * 102, y=-(row * 102) + YOFFSET)
        self.turtlesize(stretch_wid=BUTTON_STRETCH, stretch_len=BUTTON_STRETCH)
        self.onclick(self.my_click_handler)
        self.showturtle()

    def my_click_handler(self, *_):
        self.onclick(None)  # disable button
        Button.callback(self)  # call the contoller function

    def draw_symbol(self, symbol: str):
        self.write(symbol, align="center", font=FONT)


class Model:
    def __init__(self, size: int = 3):
        self.size = size
        self.data = [[FILLER for _ in range(size)] for _ in range(size)]

    def update_state(self, symbol: str, row: int, column: int):
        self.data[row][column] = symbol

    def __repr__(self) -> str:
        text = "\n"
        for row in self.data:
            text += "\n" + "|".join(row)
        return text


class View:
    def __init__(self, callback: Callable, size: int = 3):
        Button.callback = callback  # same callback for all buttons.
        for row in range(size):
            for column in range(size):
                button = Button(row, column)


class Controller:
    def __init__(self, model: Model):
        self.counter = model.size ** 2
        self.model = model
        self.PLAYERS = "XO"
        self.next_player = 0

    def get_next_player(self) -> str:
        player = self.PLAYERS[self.next_player]
        self.next_player = (self.next_player + 1) % 2
        return player

    def click_handler(self, button: Button) -> bool:
        symbol = self.get_next_player()
        button.draw_symbol(symbol)
        row, column = button.id
        self.model.update_state(symbol, row, column)
        self.counter -= 1
        return self.keep_playing()

    def keep_playing(self) -> bool:
        if self.counter > 0:
            return True
        print("game over man")
        print(self.model)
        sys.exit(0)


def main():
    model = Model(size=3)
    controller = Controller(model)
    view = View(controller.click_handler, size=model.size)
    screen = Screen()
    screen.mainloop()


if __name__ == "__main__":
    main()

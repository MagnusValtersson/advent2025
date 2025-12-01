from tkinter import *
from functools import partial
import importlib
from day1 import Day1

class MainMenu():
    def __init__(self, title, geometry):
        self.root=Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.textBox = Text(self.root, height = 5, width = 52)
        self.buttons = {}

    def finalize(self):
        self.textBox.pack()
        for key in self.buttons:
            self.buttons[key].pack()
        self.root.mainloop()

    def addButton(self, name, day):
        self.buttons[name] = Button(self.root, text=name, anchor="center", cursor="hand2", pady=5, width=4, height=1, command = partial(menu.insertText, day))

    def insertText(self, dayNr):
        day = dayNr()
        self.textBox.delete('1.0', END)
        self.textBox.insert(END, day.getAnswer() + '\n')

if __name__ == "__main__":
    menu = MainMenu("Advent of Code 2025", "600x600")
    day1 = Day1()
    menu.addButton("Day1", Day1)
    menu.addButton("Day2", Day1)
    menu.finalize()

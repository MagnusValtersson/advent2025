from tkinter import *
from functools import partial
import importlib
import day1
import day2
import day3
import day4

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
        importlib.reload(day1)
        importlib.reload(day2)
        importlib.reload(day3)
        importlib.reload(day4)
        day = dayNr()
        self.textBox.delete('1.0', END)
        self.textBox.insert(END, day.getAnswer() + '\n')

if __name__ == "__main__":
    menu = MainMenu("Advent of Code 2025", "600x600")
    menu.addButton("Day1", day1.Day1)
    menu.addButton("Day2", day2.Day2)
    menu.addButton("Day3", day3.Day3)
    menu.addButton("Day4", day4.Day4)
    menu.finalize()

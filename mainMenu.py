from tkinter import *
import testScript
import importlib

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

    def addButton(self, name, func):
        self.buttons[name] = Button(self.root, text=name, anchor="center", cursor="hand2", pady=5, width=4, height=1, command = func)

    def insertText(self):
        importlib.reload(testScript)
        self.textBox.delete('1.0', END)
        self.textBox.insert(END, testScript.getTestText() + '\n')



if __name__ == "__main__":
    menu = MainMenu("Advent of Code 2025", "600x600")
    # root = Tk()
    # root.title("Advent of Code 2025")
    # root.geometry("600x600")
    # textBox = Text(root, height = 5, width = 52)
    menu.addButton("Day1", menu.insertText)
    menu.addButton("Day2", menu.insertText)
    menu.finalize()
    # button = Button(root, text="Day1", anchor="center", cursor="hand2", pady=5, width=4, height=1, command = insertText)
    # textBox.pack()
    # button.pack()
    # root.mainloop()

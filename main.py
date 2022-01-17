#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import random
# from tkinter import ttk

"""
class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

        btn = tk.Button(self, text="Konec", command=self.close)
        btn.pack()

    def close(self):
        self.destroy()
"""

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "maTYČKA"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.lbl = tk.Label(self, text="Hello World")
        self.lbl.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack()

    def priklad(self):
        random.choice([self.plus, self.minus, self.krat, self.deleno])
        return None

    def plus(self):
        self.lbl.config(text = "+")
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, 100 - self.cisloA)
        self.vysledek = self.cisloA + self.cisloB
        return self.vysledek
    
    def minus(self):
        self.lbl.config(text = "-")
        self.cisloA = random.randint(1, 100)
        self.cisloB = random.randint(1, 100)
        if self.cisloA < self.cisloB:
            self.cisloA, self.cisloB = self.cisloB, self.cisloA
        self.vysledek = self.cisloA + self.cisloB
        return self.vysledek
    
    def krat(self):
        self.lbl.config(text = "×")
        self.cisloA = random.randint(1, 10)
        self.cisloB = random.randint(1, 10)
        self.vysledek = self.cisloA * self.cisloB
        return self.vysledek
    
    def deleno(self):
        self.lbl.config(text = "/")
        self.vysledek = random.randint(1, 9)
        self.cisloB = random.randint(1, 9)
        self.cisloA = self.vysledek * self.cisloB
        return self.vysledek


    def quit(self, event = None):
        super().quit()


app = Application()
app.mainloop()

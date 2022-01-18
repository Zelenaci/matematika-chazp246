from os.path import basename, splitext
import tkinter as tk
from tkinter import messagebox
import random

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "maTYČKA"
    
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.bind("<Return>", self.validate)
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.varEntry = tk.StringVar()
        self.varSpravny = 0
        self.varCelkem = 0

        self.frame = tk.Frame(self, highlightbackground = "#000000", highlightthickness = 2)
        self.frame.pack(padx = 50, pady = 25)        
        self.lblA = tk.Label(self.frame, text="A")
        self.lblA.pack(side = tk.LEFT, anchor = tk.S, ipadx = 5, ipady = 5)
        self.lblAkce = tk.Label(self.frame, text="+")
        self.lblAkce.pack(side = tk.LEFT, anchor = tk.S, ipadx = 5, ipady = 5)
        self.lblB = tk.Label(self.frame, text="B")
        self.lblB.pack(side = tk.LEFT, anchor = tk.S, ipadx = 5, ipady = 5)
        vcmd = (self.register(self.callback))
        self.entry = tk.Entry(self.frame, validate="all", validatecommand=(vcmd, '%P'), width = 3, textvariable = self.varEntry)
        self.entry.pack(side = tk.LEFT, anchor = tk.S, padx = 5, pady = 5)
        self.btnValidate = tk.Button(self.frame, text="Validate", command=self.validate)
        self.btnValidate.pack(side = tk.LEFT, anchor = tk.S, padx = 5, pady = 5)

        self.btn = tk.Button(self.frame, text="Quit", command=self.quit)
        self.btn.pack(side = tk.LEFT, anchor = tk.S, padx = 5, pady = 5)

        self.priklad()


    def callback(self, P):
        if str.isdigit(P) or P == "":
            return True
        else:
            return False


    def priklad(self):
        vysledek = random.choice([self.plus, self.minus, self.krat, self.deleno])
        return vysledek()

    def validate(self, event = None):
        try:
            user_vysledek = int(self.varEntry.get())
        except:
            user_vysledek = ""

        self.varEntry.set("")
        if self.vysledek == user_vysledek:
            self.varSpravny = self.varSpravny + 1
            self.varCelkem = self.varCelkem + 1
            self.config(background="#609c49")
            print("Spravně")
        else:
            self.varCelkem = self.varCelkem + 1
            self.config(background="#a3110f")
            print("dum dum")
        self.priklad()
        
    def plus(self):
        self.lblAkce.config(text = "+")
        self.cisloA = random.randint(1, 99)
        self.cisloB = random.randint(1, 100 - self.cisloA)
        self.lblA.config(text = self.cisloA)
        self.lblB.config(text = self.cisloB)
        self.vysledek = self.cisloA + self.cisloB
        return self.vysledek
    
    def minus(self):
        self.lblAkce.config(text = "-")
        self.cisloA = random.randint(1, 100)
        self.cisloB = random.randint(1, 100)
        if self.cisloA < self.cisloB:
            self.cisloA, self.cisloB = self.cisloB, self.cisloA
        self.vysledek = self.cisloA - self.cisloB
        self.lblA.config(text = self.cisloA)
        self.lblB.config(text = self.cisloB)
        return self.vysledek
    
    def krat(self):
        self.lblAkce.config(text = "×")
        self.cisloA = random.randint(1, 10)
        self.cisloB = random.randint(1, 10)
        self.vysledek = self.cisloA * self.cisloB
        self.lblA.config(text = self.cisloA)
        self.lblB.config(text = self.cisloB)
        return self.vysledek
    
    def deleno(self):
        self.lblAkce.config(text = "/")
        self.vysledek = random.randint(1, 9)
        self.cisloB = random.randint(1, 9)
        self.cisloA = self.vysledek * self.cisloB
        self.lblA.config(text = self.cisloA)
        self.lblB.config(text = self.cisloB)
        return self.vysledek


    def quit(self, event = None):
        if self.varSpravny != 0:
            self.procenta = self.varSpravny / self.varCelkem * 100
        else:
            self.procenta = 0   
        messagebox.showinfo("Report", f"Celkem: {self.varCelkem}\nSprávné odpovědi: {self.varSpravny}\nŠpatně: {self.varCelkem - self.varSpravny}\nProcenta: {self.procenta} %") 
        super().quit()


app = Application()
app.mainloop()

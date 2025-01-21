import turtle as t
import tkinter as tk

FONT = ("Courier", 55, "normal")

class Stopwatch(t.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-120, 0)
        self.write("00:00:00", font=FONT)




TIMES = [1,5,10,15,30,60]
class TimeOptions:
    def __init__(self):
        self.listbox = tk.Listbox(height=4, width=20)
        self.listbox.place()
        for time in TIMES:
            self.listbox.insert(tk.END, time)



    def options(self):
        pass

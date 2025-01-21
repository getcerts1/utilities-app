import turtle as t
from stopwatch_oop import Stopwatch
from stopwatch_oop import TimeOptions
import time

screen = t.Screen()
screen.setup(600,400)
screen.bgcolor("white")
root = screen._root
root.resizable(False, False)
screen.tracer()



stopwatch = Stopwatch()
time_options = TimeOptions()

while True:
    screen.update()
    time.sleep(0.1)

    t.done()
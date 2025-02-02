import math
from tkinter import *
from tkinter import messagebox

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
TIMES = [5, 10, 15, 30, 45]

selected_time = 0
canvas = None
timer_text = None
timer = None
reset_button = None

def reset():
    global canvas, reset_button
    screen.after_cancel(timer)
    canvas.place_forget()
    reset_button.place_forget()
    timer_list_box.selection_clear(0, END)
    timer_list_box.place(x=125, y=155)


def countdown(count):
    global timer_text, timer
    minutes = math.floor(count / 60)
    seconds = count % 60

    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = screen.after(1000, countdown, count - 1)
    elif count < 0:
        message = messagebox.showinfo(title="Time up", message="TIME IS UP\n\n reset?")
        if message:
            countdown(selected_time * 60)


def timer_func(event):
    global selected_time, canvas, timer_text, reset_button
    selected_time = int(timer_list_box.get(timer_list_box.curselection()))
    seconds_convert = selected_time * 60

    if selected_time == 60:
        timer_set = '1:00:00'
        print(seconds_convert)
    else:
        timer_set = f"{seconds_convert}:00"


    timer_list_box.place_forget()

    canvas = Canvas(width=300, height=200, highlightthickness=0)
    canvas.config(bg=YELLOW)
    canvas.place(x=75, y=125)

    timer_text = canvas.create_text(
        135, 85, text=timer_set, fill="black", font=(FONT_NAME, 75, "bold")
    )

    reset_button = Button(text="RESET", font=(FONT_NAME, 24, "bold"), highlightthickness=0,
                          fg="black", command=reset)
    reset_button.place(x=150,y=300)
    countdown(seconds_convert)


screen = Tk()
screen.minsize(400, 400)
screen.config(bg=YELLOW)
screen.resizable(False, False)

label = Label(text="TIMER", font=(FONT_NAME, 35, "normal"), fg=PINK, bg=YELLOW)
label.grid(column=0, row=0, columnspan=3, padx=150, pady=20)

timer_list_box = Listbox(height=len(TIMES), width=20)
timer_list_box.place(x=125, y=155)
for item in TIMES:
    timer_list_box.insert(END, item)
timer_list_box.bind("<Double-Button-1>", timer_func)




screen.mainloop()

import tkinter as tk

window = tk.Tk()
window.minsize(300,300)
window.title("Calculator")
window.resizable(False, False)
FONT = ('Arial', 18, "normal")


equation = ""

def calculate():
    global equation
    result = str(round(eval(equation), 2))
    entry.delete(0, tk.END)
    entry.insert(0, result)
    equation = result

def add_to_equation(value):
    global equation
    equation += value
    entry.delete(0, tk.END)
    entry.insert(0, equation)

def clear_entry():
    global equation
    equation = ""
    entry.delete(0, tk.END)
    entry.insert(0, "0")

entry = tk.Entry(width=40)
entry.insert(0, "0")
entry.grid(row=0, column=0,columnspan=10)



buttons = [
    ('1', 1, 1), ('2', 1, 2), ('3', 1, 3), ('/', 1, 4),
    ('4', 2, 1), ('5', 2, 2), ('6', 2, 3), ('*', 2, 4),
    ('7', 3, 1), ('8', 3, 2), ('9', 3, 3), ('-', 3, 4),
    ('C', 4, 1), ('0', 4, 2), ('=', 4, 3), ('+', 4, 4),
]


for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, width=5, height=2, font=FONT, command=calculate)
    elif text == 'C':
        button = tk.Button(window, text=text, width=5, height=2, font=FONT, command=clear_entry)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=FONT,
                           command=lambda value=text: add_to_equation(value))

    button.grid(row=row, column=col, padx=5, pady=5)





window.mainloop()

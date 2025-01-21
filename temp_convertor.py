import tkinter as tk

screen = tk.Tk()
screen.minsize(width=350, height=200)
screen.title("Temp convertor")
screen.resizable(False, False)



#Format

#       LABEL
#   ENTRY LABEL(CELSIUS)
#   LABEL(IS EQUAL TO) LABEL(VALUE) LABEL(FAHRENHEIT)
#            BUTTON(CONVERT)  BUTTON(RESET)


label = tk.Label(text="Temp App", font=("Courier", 26, "normal"))
label.grid(row=0, column=0, columnspan=3, pady=(10, 20))  # Centered and spaced out

entry = tk.Entry(width=10)
entry.grid(row=1, column=1, padx=5, pady=5)

Celsius_label = tk.Label(text="Celsius", font=("Courier", 16, "normal"))
Celsius_label.grid(row=1, column=2, padx=5, pady=5)

is_equal_to = tk.Label(text="is equal to", font=("Courier", 16, "normal"))
is_equal_to.grid(row=2, column=0, padx=5, pady=5)

Fahrenheit = tk.Label(text="0", font=("Courier", 24, "normal"))
Fahrenheit.grid(row=2, column=1, padx=5, pady=5)

result_unit_label = tk.Label(text="Fahrenheit", font=("Courier", 16, "normal"))
result_unit_label.grid(row=2, column=2, padx=5, pady=5)

def convert():
    value = float(entry.get())
    far = (value * 9/5) + 32
    Fahrenheit["text"] = round(far, 2)

def clear():
    entry.delete(0, tk.END)
    Fahrenheit["text"] = "0"


convert_button = tk.Button(text="CONVERT", font=("Courier", 16, "normal"), command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

clear_button = tk.Button(text="CLEAR", font=("Courier", 16, "normal"), command=clear)
clear_button.grid(row=3, column=1, columnspan=3,pady=10)



screen.mainloop()






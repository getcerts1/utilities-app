import tkinter as tk
import random
import os

def change_color():
    random_color = f"#{random.randint(0, 0xFFFFFF):06x}"
    window.config(bg=random_color)
    window.after(10000, change_color)

window = tk.Tk()
window.minsize(height=300, width=300)
window.title("Utilities App")
change_color()

label = tk.Label(text="UTILITIES", font=("Courier", 26, "italic"))
label.grid(column=0, row=0, columnspan=3, padx=50, pady=(20, 40))

utilities = {
    "Miles convertor": "./miles_convertor.py",
    "Temp convertor": "./temp_convertor.py",
    "Stopwatch": "./stopwatch.py",
    "calculator": "./calculator.py",
}

def listbox_used(event):
    selected_item = listbox.get(listbox.curselection())
    if selected_item in utilities and os.path.exists(utilities[selected_item]):
        os.system(f"python {utilities[selected_item]}")
    else:
        print(f"The utility '{selected_item}' is not available.")

listbox = tk.Listbox(height=4, width=20)
listbox.grid(column=0, row=1, columnspan=3, padx=50, pady=(20, 20))

for utility in utilities.keys():
    listbox.insert(tk.END, utility)

listbox.bind("<<ListboxSelect>>", listbox_used)

window.mainloop()

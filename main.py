import tkinter as tk
import random
import os
from tkinter import messagebox

def change_color():
    output = random_color = f"#{random.randint(0, 0xFFFFFF):06x}"
    window.config(bg=random_color)
    window.after(10000, change_color)
    return output
def update_label_color():
    new_color = change_color()
    label.config(bg=new_color)
    window.after(10000, update_label_color)


window = tk.Tk()
window.minsize(height=300, width=300)
window.resizable(False,False)
window.title("Utilities App")
change_color()

label = tk.Label(text="UTILITIES", font=("Courier", 26, "italic"))
label.grid(column=0, row=0, columnspan=3, padx=50, pady=(20, 40))
update_label_color()

utilities = {
    "Miles convertor": "./miles_convertor.py",
    "Temp convertor": "./temp_convertor.py",
    "Stopwatch": "./stopwatch.py",
    "calculator": "./calculator.py",
    "password-manager":"./password-manager/main.py"
}

def listbox_used(event):
    selected_item = listbox.get(listbox.curselection())
    if selected_item in utilities and os.path.exists(utilities[selected_item]):
        os.system(f"python {utilities[selected_item]}")
    else:
        print(f"The utility '{selected_item}' is not available.")
        messagebox.showinfo(title="error", message=f"The utility '{selected_item}' is not available.")
        return

listbox = tk.Listbox(height=5, width=20)
listbox.grid(column=0, row=1, columnspan=3, padx=50, pady=20)

for utility in utilities.keys():
    listbox.insert(tk.END, utility)

listbox.bind("<Double-Button-1>", listbox_used)

window.mainloop()

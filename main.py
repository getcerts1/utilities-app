import tkinter as tk
import random

def change_color():
    random_color = f"#{random.randint(0, 0xFFFFFF):06x}"
    window.config(bg=random_color)
    window.after(20000, change_color)

window = tk.Tk()
window.minsize(height=300, width=300)
change_color()

label = tk.Label(text="UTILITIES", font=("Courier", 26, "italic"))
label.grid(column=0, row=0, columnspan=3, padx=100, pady=(20,40))

def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4, width=15)
listbox.grid(column=2, row=1, columnspan= 3, padx=100, pady=(20,20))
fruits = ["Miles convertor", "Temp convertor", "Stopwatch", "calculator"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)



window.mainloop()
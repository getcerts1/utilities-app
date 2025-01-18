import tkinter as tk

# Create the main application window
rootscreen = tk.Tk()
rootscreen.title("Converter")
rootscreen.minsize(width=350, height=200)


label = tk.Label(text="Converter App", font=("Courier", 26, "normal"))
label.grid(row=0, column=0, columnspan=3, pady=(10, 20))  # Centered and spaced out

entry = tk.Entry(width=10)
entry.grid(row=1, column=1, padx=5, pady=5)

miles_label = tk.Label(text="Miles", font=("Courier", 16, "normal"))
miles_label.grid(row=1, column=2, padx=5, pady=5)

is_equal_to = tk.Label(text="is equal to", font=("Courier", 16, "normal"))
is_equal_to.grid(row=2, column=0, padx=5, pady=5)

miles_value = tk.Label(text="0", font=("Courier", 24, "normal"))
miles_value.grid(row=2, column=1, padx=5, pady=5)

result_unit_label = tk.Label(text="Kilometers", font=("Courier", 16, "normal"))
result_unit_label.grid(row=2, column=2, padx=5, pady=5)

def convert():
    value = float(entry.get())
    if value == 0:
        miles_value["text"] = "0"
    else:
        km = value * 1.6
        miles_value["text"] = round(km, 2)


convert_button = tk.Button(text="Convert", font=("Courier", 16, "normal"), command=convert)
convert_button.grid(row=3, column=1, pady=(10, 0))

return_button = tk.Button(text="RETURN", font=("Courier", 16, "normal"))
return_button.grid(row=4, column=1, pady=(10, 0))



rootscreen.mainloop()




















rootscreen.mainloop()

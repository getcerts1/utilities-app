from tkinter import *
import pandas as pd
import os
import string, random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    ascii_letters = string.ascii_letters
    numbers = string.digits

    characters = ascii_letters + numbers*2
    random_str = "".join(random.choice(characters) for i in range(random.randint(15,17)))
    password_entry.insert(string=f"{random_str}", index=0)
    print(random_str)
    return random_str

# ---------------------------- SAVE PASSWORD ------------------------------- #
def retrieve_info():
    data = []

    #retrieve all input and strip
    website_output = website_entry.get().strip()
    user_output = user_entry.get().strip()
    password_output = password_entry.get().strip()

    #if value is empty then request input and delete lines
    if not website_output or not user_output or not password_output:
        print("Enter a value")
        website_entry.delete(0, END)
        user_entry.delete(0, END)
        password_entry.delete(0, END)
        return

    #else take value and append a dict to a list
    data.append({
        "Website": website_output,
        "User": user_output,
        "Password": password_output
    })

    #create a dataframe from the list (pandas dataframe only takes input in the form of a list)
    df = pd.DataFrame(data)

    #check if file path exists, if so append else, create a new file
    file_path = "password_app_data.csv"
    if os.path.exists(file_path):
        df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        df.to_csv(file_path, index=False)


    #Delete entry for new user
    website_entry.delete(0, END)
    user_entry.delete(0, END)
    password_entry.delete(0, END)



    # ---------------------------- UI SETUP ------------------------------- #
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, 'logo.png')

FONT_NAME = "Arial"
FONT_SIZE = 14
FONT_SHAPE = "bold"
screen = Tk()
#screen.minsize(500,500)
screen.resizable(False, False)
screen.title("Password manager")
screen.config(padx=40,pady=40)



canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.grid(row=0, column=1)
photo = PhotoImage(file=image_path)
create_image = canvas.create_image(100,100, image=photo)

website_label = Label(text="Website:", font=(FONT_NAME,FONT_SIZE, FONT_SHAPE))
website_label.grid(row=1, column=0)
website_label.config(fg="white")

user_label = Label(text="Email/Username:", font=(FONT_NAME,FONT_SIZE, FONT_SHAPE))
user_label.grid(row=2, column=0)
user_label.config(fg="white")

password_label = Label(text="Password:", font=(FONT_NAME,FONT_SIZE, FONT_SHAPE))
password_label.grid(row=3, column=0)
password_label.config(fg="white")

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.config(fg="white")

user_entry = Entry(width=35)
user_entry.grid(row=2, column=1, columnspan=2)
user_entry.config(fg="white")

password_entry = Entry(width=18)
password_entry.grid(row=3, column=1)
password_entry.config(fg="white")

generate_button = Button(text="generate password", fg="black", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=33, command=retrieve_info)
add_button.grid(row=4, column=1, columnspan=4)



screen.mainloop()
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, 'end')

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }

    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Empty Fields", message="Do not leave empty fields")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)

        finally:
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showerror(title="Empty Fields", message="Do not leave empty fields")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror(title="EmptyDB", message="The password DB is Empty")
        else:
            if website in data:
                username = data[website]["username"]
                password = data[website]["password"]
                messagebox.showinfo(title="Password", message=f"username: {username}\n,password: {password}")
            else:
                messagebox.showerror(title="No Website", message="Website not found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pass")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

website_label = Label(text="Website")
username_label = Label(text="Username")
password_label = Label(text="Password")

website_entry = Entry()
website_entry.config(width=33)
website_entry.focus()
website_entry.grid(column=1, row=1)

username_entry = Entry()
username_entry.config(width=52)
username_entry.insert(0, "richardjohnsmith@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry()
password_entry.config(width=33)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", command=search, width=14)
search_button.grid(column=2, row=1
                   )
generate_button = Button(text="Generate Password", command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save)
add_button.config(width=44)
add_button.grid(column=1, row=4, columnspan=2)

canvas.grid(column=1, row=0)

website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

window.mainloop()

from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generator():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")

    password_lst = list()

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_lst = password_letters + password_symbols + password_numbers
    shuffle(password_lst)
    password_generated = "".join(password_lst)
    password_entry.insert(0, password_generated)
    pyperclip.copy(password_generated)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    json_dic = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opppsss", message="Your fields are empty renter again")
    else:
        fine = messagebox.askokcancel(title="Confirmation",
                                      message=f"website:{website}\n email:{email}\n password:{password}")
        if fine:
            try:
                with open("data.json", "r") as data_file:
                    # data_file.write(f"{website} | {email} | {password}\n")
                    data = json.load(data_file)
            except:
                with open("data.json", "w") as data_file:
                    json.dump(json_dic, data_file, indent=4)
            else:
                data.update(json_dic)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def search():
    website = website_entry.get()
    with open("data.json", "r") as data_file:
        data = json.load(data_file)

        try:
            value = data[website]
            messagebox.showinfo(title="This is your details",
                                message=f"email:{value['email']}\npassword:{value['password']}")
            pyperclip.copy(value['password'])
        except:
            messagebox.showinfo(title="Opppsss", message="Cannot find the website")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)

logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
# Labels
website_label = Label(text="Website:")
email_label = Label(text="Email/Username:")
password_label = Label(text="Password:")
website_label.grid(column=0, row=1)
email_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)
# Entry
website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(column=1, row=1)
email_entry = Entry(width=53)
email_entry.insert(0, "hello@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)
# Buttons
search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1, columnspan=2)
password_button = Button(text="Generate password", command=generator)
add_button = Button(text="Add", width=45, command=save)
password_button.grid(column=2, row=3)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()

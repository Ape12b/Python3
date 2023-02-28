from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    entry_password.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + \
                    [random.choice(symbols) for _ in range(nr_symbols)] + \
                    [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = ''.join(password_list)
    entry_password.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password(entry_password, entry_username, entry_website):
    password = entry_password.get()
    email = entry_username.get()
    website = entry_website.get()

    option = messagebox.askokcancel(title=website, message=f"Details: \nEmail: {email}\nPassword: {password}\nOkay?")

    if option:
        if len(password) == 0:
            messagebox.showinfo(title="Error", message="Please enter a valid password!")
        elif len(website) == 0:
            messagebox.showinfo(title="Error", message="Please enter a valid Website!")
        else:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
                entry_password.delete(0, END)
                entry_website.delete(0, END)
                entry_website.focus()
                pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=50, padx=50)
window.title("Password Manager")
image_logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=image_logo)
canvas.grid(row=0, column=1)

label_w = Label(text="Website:")
label_w.grid(row=1, column=0)

entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0)

entry_email = Entry(width=35)
entry_email.grid(row=2, column=1, columnspan=2)
entry_email.insert(0, "apri4u@gmail.com")

label_p = Label(text="Password:")
label_p.grid(row=3, column=0)

entry_password = Entry(width=22)
entry_password.grid(row=3, column=1)

button_gen = Button(text="Generate Password", font=("Ariel", 10), command=generate_password)
button_gen.grid(row=3, column=2)

button_gen = Button(text="Add", font=("Ariel", 10), width=43, command=lambda
    entry_password=entry_password, entry_website=entry_website, entry_username=entry_email: add_password(entry_password,
                                                                                                         entry_username,
                                                                                                         entry_website))

button_gen.grid(row=4, column=1, columnspan=2)

window.mainloop()

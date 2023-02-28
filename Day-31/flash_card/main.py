import random
from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/spanish_words.csv")

data_dict = data.to_dict(orient="records")
words_learned = {"Spanish": [], "English": []}
word = random.choice(data_dict)


def learned():
    global after_id
    data_dict.remove(word)
    words_learned["Spanish"].append(word["Spanish"])
    words_learned["English"].append(word["English"])
    new_card()


def not_learned():
    global after_id
    new_card()


def new_card():
    global word
    global after_id
    try:
        window.after_cancel(after_id)
    except ValueError:
        pass
    word = random.choice(data_dict)
    canvas.itemconfig(canvas_image, image=front_image)
    canvas.itemconfig(text_title, text="Spanish", fill="green")
    canvas.itemconfig(text_French, text=word["Spanish"], fill="green")
    after_id = window.after(3000, func=flip_card)


def flip_card():
    global word
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(text_title, text="English", fill="white")
    canvas.itemconfig(text_French, text=word["English"], fill="white")


window = Tk()
window.title("Flash Card App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

after_id = window.after(3000, func=flip_card)

front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

canvas_image = canvas.create_image(400, 266, image=front_image)
text_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
text_French = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

button = Button(command=not_learned)
button.config(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR)
button.grid(row=1, column=0)

button = Button(command=learned)
button.config(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR)
button.grid(row=1, column=1)

not_learned()

window.mainloop()

df = pandas.DataFrame(data_dict)
df.to_csv("./data/to_learn.csv", index=False)

from tkinter import *

window = Tk()
window.minsize(width=500, height=400)


def change_label():
    label["text"] = input_arg.get()


label = Label(text="I am a label!")
label.grid(column=0, row=0)

button = Button(text="Click me!", command=change_label)
button.grid(column=1, row=1)

input_arg = Entry()
input_arg.grid(column=4, row=3)

button2 = Button(text="Push!")
button2.grid(column=2, row=0)

window.mainloop()

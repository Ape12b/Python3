from tkinter import *


window = Tk()
window.minsize(width=200, height=100)


def get_km():
    input_miles = int(input_entry.get())
    label_op.config(text=f"{round(input_miles * 1.61, 2)}")


input_entry = Entry(width=10)
input_entry.grid(row=0, column=1, rowspan=2)

label_miles = Label(text="Miles")
label_miles.grid(row=0, column=2, rowspan=2)

label_text = Label(text="is equal to")
label_text.grid(row=2, column=0)

label_km = Label(text="km")
label_km.grid(row=2, column=2)

label_op = Label(text="0")
label_op.grid(row=2, column=1)

button = Button(text="Calculate", command=get_km)
button.grid(row=4, column=1)

window.mainloop()

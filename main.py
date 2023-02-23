import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title("Invoice Maker Form")

frame = tkinter.Frame(window)
frame.pack()

# Creating the First Name label on the GUI
first_name_label = tkinter.Label(frame, text="First Name")
first_name_label.grid(row=0, column=0)

# Creating the Last Name label on the GUI
last_name_label = tkinter.Label(frame, text="Last Name")
last_name_label.grid(row=0, column=1)

# Creating input boxes for First and Last names
first_name_entry = tkinter.Entry(frame)
last_name_entry = tkinter.Entry(frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

phone_label = tkinter.Label(frame, text="Phone")
phone_label.grid(row=0, column=2)
phone_entry = tkinter.Entry(frame)
phone_entry.grid(row=1, column=2)

quantity_label = tkinter.Label(frame, text="Quantity")
quantity_label.grid(row=2, column=0)
quantity_entry = tkinter.Spinbox(frame, from_=1, to=100)
quantity_entry.grid(row=3, column=0)

description_label = tkinter.Label(frame, text="Description")
description_label.grid(row=2, column=1)
description_entry = tkinter.Entry(frame)
description_entry.grid(row=3, column=1)

unit_price_label = tkinter.Label(frame, text="Unit Price")
unit_price_label.grid(row=2, column=2)
unit_price_entry = tkinter.Spinbox(frame, from_=1, to=100)
unit_price_entry.grid(row=3, column=2)



window.mainloop()

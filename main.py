import tkinter
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox


def clear_item():
    quantity_entry.delete(0, tkinter.END)
    quantity_entry.insert(0, "1")
    description_entry.delete(0, tkinter.END)
    unit_price_entry.delete(0, tkinter.END)
    unit_price_entry.insert(0, "0.0")


invoice_list = []


def add_item():
    qty = int(quantity_entry.get())
    desc = description_entry.get()
    price = float(unit_price_entry.get())
    line_total = qty * price
    invoice_item = [qty, desc, price, line_total]

    tree.insert('', 0, values=invoice_item)
    clear_item()
    invoice_list.append(invoice_item)


def new_invoice():
    first_name_entry.delete(0, tkinter.END)
    last_name_entry.delete(0, tkinter.END)
    phone_entry.delete(0, tkinter.END)
    clear_item()
    tree.delete(*tree.get_children())
    invoice_list.clear()


def generate_invoice():
    doc = DocxTemplate("invoice_template.docx")
    name = first_name_entry.get() + " " + last_name_entry.get()
    phone = phone_entry.get()
    subtotal = sum(item[3] for item in invoice_list)
    salestax = 0.05
    total = subtotal * (1 + salestax)
    new_total = round(total, 2)

    doc.render({"name": name, "phone": phone, "invoice_list": invoice_list, "subtotal": subtotal,
                "salestax": str(salestax * 100) + "%", "total": new_total})
    doc_name = "new_invoice" + name + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(doc_name)

    messagebox.showinfo("Invoice Complete", "Invoice Generated")
    new_invoice()


window = tkinter.Tk()
window.title("Invoice Maker Form")

frame = tkinter.Frame(window)
frame.pack(padx=20, pady=10)

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
unit_price_entry = tkinter.Spinbox(frame, from_=0.0, to=500, increment=0.5)
unit_price_entry.grid(row=3, column=2)

add_button = tkinter.Button(frame, text="Add Item", command=add_item)
add_button.grid(row=4, column=2, pady=5)

columns = ('Qty', 'Description', 'Price', 'Total')
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading('Qty', text='Qty')
tree.heading('Description', text='Description')
tree.heading('Price', text='Price')
tree.heading('Total', text='Total')

tree.grid(row=5, column=0, columnspan=3, padx=20, pady=10)

generate_button = tkinter.Button(frame, text="Generate Invoice", command=generate_invoice)
generate_button.grid(row=6, column=0, columnspan=3, sticky="ew", padx=20, pady=5)

new_button = tkinter.Button(frame, text="New Invoice", command=new_invoice)
new_button.grid(row=7, column=0, columnspan=3, sticky="ew", padx=20, pady=5)

window.mainloop()

import tkinter as tk
from tkinter import ttk, messagebox


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Mobile Shop Management System")
root.geometry("950x600")
root.resizable(False, False)


# ---------------- FUNCTIONS ----------------
def add_mobile():
    mobile_id = entry_id.get()
    name = entry_name.get()
    brand = entry_brand.get()
    price = entry_price.get()
    quantity = entry_quantity.get()

    if mobile_id == "" or name == "" or brand == "" or price == "" or quantity == "":
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        float(price)
        int(quantity)
    except ValueError:
        messagebox.showerror("Error", "Price and Quantity must be numbers")
        return

    # Check duplicate ID
    for item in table.get_children():
        values = table.item(item, "values")
        if values[0] == mobile_id:
            messagebox.showerror("Error", "Mobile ID already exists")
            return

    table.insert(
        "",
        tk.END,
        values=(mobile_id, name, brand, price, quantity)
    )

    clear_fields()
    messagebox.showinfo("Success", "Mobile added successfully")


def delete_mobile():
    selected = table.selection()

    if not selected:
        messagebox.showwarning("Warning", "Please select a mobile")
        return

    for item in selected:
        table.delete(item)

    messagebox.showinfo("Success", "Mobile deleted successfully")


def sell_mobile():
    selected = table.selection()

    if not selected:
        messagebox.showwarning("Warning", "Please select a mobile")
        return

    item = selected[0]
    values = table.item(item, "values")

    quantity = int(values[4])

    if quantity <= 0:
        messagebox.showerror("Error", "Mobile is out of stock")
        return

    quantity -= 1

    table.item(
        item,
        values=(values[0], values[1], values[2], values[3], quantity)
    )

    total = float(values[3])

    messagebox.showinfo(
        "Sale Successful",
        f"Mobile Sold Successfully!\n\n"
        f"Mobile: {values[1]}\n"
        f"Price: ₹{total:.2f}\n"
        f"Remaining Stock: {quantity}"
    )


def search_mobile():
    search_text = entry_search.get().lower()

    for item in table.get_children():
        values = table.item(item, "values")

        if (
            search_text in values[0].lower()
            or search_text in values[1].lower()
            or search_text in values[2].lower()
        ):
            table.selection_set(item)
            table.focus(item)
            table.see(item)
            return

    messagebox.showinfo("Search", "Mobile not found")


def clear_search():
    entry_search.delete(0, tk.END)
    table.selection_remove(table.selection())


def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_brand.delete(0, tk.END)
    entry_price.delete(0, tk.END)
    entry_quantity.delete(0, tk.END)


# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="MOBILE SHOP MANAGEMENT SYSTEM",
    font=("Arial", 22, "bold")
)
title.pack(pady=15)


# ---------------- INPUT FRAME ----------------
input_frame = tk.LabelFrame(
    root,
    text="Mobile Details",
    font=("Arial", 12, "bold"),
    padx=10,
    pady=10
)
input_frame.pack(fill="x", padx=20)


# Mobile ID
tk.Label(input_frame, text="Mobile ID").grid(
    row=0, column=0, padx=10, pady=5
)

entry_id = tk.Entry(input_frame, width=20)
entry_id.grid(row=0, column=1, padx=10)


# Mobile Name
tk.Label(input_frame, text="Mobile Name").grid(
    row=0, column=2, padx=10
)

entry_name = tk.Entry(input_frame, width=20)
entry_name.grid(row=0, column=3, padx=10)


# Brand
tk.Label(input_frame, text="Brand").grid(
    row=1, column=0, padx=10, pady=5
)

entry_brand = tk.Entry(input_frame, width=20)
entry_brand.grid(row=1, column=1, padx=10)


# Price
tk.Label(input_frame, text="Price").grid(
    row=1, column=2, padx=10
)

entry_price = tk.Entry(input_frame, width=20)
entry_price.grid(row=1, column=3, padx=10)


# Quantity
tk.Label(input_frame, text="Quantity").grid(
    row=2, column=0, padx=10, pady=5
)

entry_quantity = tk.Entry(input_frame, width=20)
entry_quantity.grid(row=2, column=1, padx=10)


# ---------------- BUTTONS ----------------
button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(
    button_frame,
    text="Add Mobile",
    width=15,
    command=add_mobile
).grid(row=0, column=0, padx=5)

tk.Button(
    button_frame,
    text="Sell Mobile",
    width=15,
    command=sell_mobile
).grid(row=0, column=1, padx=5)

tk.Button(
    button_frame,
    text="Delete Mobile",
    width=15,
    command=delete_mobile
).grid(row=0, column=2, padx=5)

tk.Button(
    button_frame,
    text="Clear Fields",
    width=15,
    command=clear_fields
).grid(row=0, column=3, padx=5)


# ---------------- SEARCH ----------------
search_frame = tk.Frame(root)
search_frame.pack(pady=5)

tk.Label(
    search_frame,
    text="Search Mobile:"
).pack(side=tk.LEFT, padx=5)

entry_search = tk.Entry(search_frame, width=30)
entry_search.pack(side=tk.LEFT, padx=5)

tk.Button(
    search_frame,
    text="Search",
    width=10,
    command=search_mobile
).pack(side=tk.LEFT, padx=5)

tk.Button(
    search_frame,
    text="Clear Search",
    width=12,
    command=clear_search
).pack(side=tk.LEFT, padx=5)


# ---------------- TABLE ----------------
table_frame = tk.Frame(root)
table_frame.pack(padx=20, pady=10, fill="both", expand=True)

columns = (
    "Mobile ID",
    "Mobile Name",
    "Brand",
    "Price",
    "Quantity"
)

table = ttk.Treeview(
    table_frame,
    columns=columns,
    show="headings",
    height=12
)

for column in columns:
    table.heading(column, text=column)
    table.column(column, width=170, anchor="center")

table.pack(side=tk.LEFT, fill="both", expand=True)


# Scrollbar
scrollbar = ttk.Scrollbar(
    table_frame,
    orient="vertical",
    command=table.yview
)

scrollbar.pack(side=tk.RIGHT, fill="y")

table.configure(yscrollcommand=scrollbar.set)


# ---------------- SAMPLE DATA ----------------
table.insert(
    "",
    tk.END,
    values=("M001", "iPhone 15", "Apple", "65000", "5")
)

table.insert(
    "",
    tk.END,
    values=("M002", "Galaxy S24", "Samsung", "70000", "4")
)

table.insert(
    "",
    tk.END,
    values=("M003", "OnePlus 12", "OnePlus", "55000", "6")
)

table.insert(
    "",
    tk.END,
    values=("M004", "Redmi Note 13", "Xiaomi", "18000", "10")
)


# ---------------- RUN ----------------
root.mainloop()

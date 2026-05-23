import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

# =========================
# SAVE EXPENSE FUNCTION
# =========================

def add_expense():

    category = category_combobox.get()
    amount = amount_entry.get()
    description = description_entry.get()

    if category == "" or amount == "":
        messagebox.showerror(
            "Error",
            "Please fill all required fields"
        )
        return

    # =========================
    # SAVE TO CSV
    # =========================

    file_exists = os.path.isfile("expenses.csv")

    with open(
        "expenses.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(
                ["Category", "Amount", "Description"]
            )

        writer.writerow(
            [category, amount, description]
        )

    # =========================
    # UPDATE TOTAL
    # =========================

    update_total()

    messagebox.showinfo(
        "Success",
        "Expense Added Successfully"
    )

    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# =========================
# UPDATE TOTAL FUNCTION
# =========================

def update_total():

    total = 0

    if os.path.isfile("expenses.csv"):

        with open("expenses.csv", "r") as file:

            reader = csv.reader(file)

            next(reader, None)

            for row in reader:

                total += float(row[1])

    total_label.config(
        text=f"Total Expense: ₹ {total:.2f}"
    )

# =========================
# GUI WINDOW
# =========================

root = tk.Tk()

root.title("Expense Tracker")

root.geometry("500x550")

root.config(bg="#1f1f2e")

# =========================
# TITLE
# =========================

title_label = tk.Label(
    root,
    text="Expense Tracker",
    font=("Helvetica", 24, "bold"),
    bg="#1f1f2e",
    fg="white"
)

title_label.pack(pady=20)

# =========================
# CATEGORY
# =========================

category_label = tk.Label(
    root,
    text="Select Category",
    font=("Helvetica", 12),
    bg="#1f1f2e",
    fg="white"
)

category_label.pack()

category_combobox = ttk.Combobox(
    root,
    values=[
        "Food",
        "Travel",
        "Shopping",
        "Bills",
        "Entertainment",
        "Other"
    ],
    font=("Helvetica", 12)
)

category_combobox.pack(pady=10)

# =========================
# AMOUNT
# =========================

amount_label = tk.Label(
    root,
    text="Enter Amount",
    font=("Helvetica", 12),
    bg="#1f1f2e",
    fg="white"
)

amount_label.pack()

amount_entry = tk.Entry(
    root,
    font=("Helvetica", 12),
    width=30
)

amount_entry.pack(pady=10)

# =========================
# DESCRIPTION
# =========================

description_label = tk.Label(
    root,
    text="Description",
    font=("Helvetica", 12),
    bg="#1f1f2e",
    fg="white"
)

description_label.pack()

description_entry = tk.Entry(
    root,
    font=("Helvetica", 12),
    width=30
)

description_entry.pack(pady=10)

# =========================
# ADD BUTTON
# =========================

add_button = tk.Button(
    root,
    text="Add Expense",
    command=add_expense,
    font=("Helvetica", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2"
)

add_button.pack(pady=20)

# =========================
# TOTAL LABEL
# =========================

total_label = tk.Label(
    root,
    text="Total Expense: ₹ 0",
    font=("Helvetica", 18, "bold"),
    bg="#1f1f2e",
    fg="#00ff99"
)

total_label.pack(pady=20)

# =========================
# LOAD TOTAL
# =========================

update_total()

# =========================
# RUN APP
# =========================

root.mainloop()
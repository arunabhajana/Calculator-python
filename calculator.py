
"""
    The code is about simple calculator application implemented using the tkinter library in Python.
"""
import tkinter as tk
from tkinter import PhotoImage

def on_click(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def delete_last():
    current = entry.get()[:-1]
    entry.delete(0, tk.END)
    entry.insert(tk.END, current)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.iconphoto(True, tk.PhotoImage(file='calc.png'))

entry = tk.Entry(root, width=20, font=('Arial', 16), justify='right', borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 16),
              command=lambda b=button: on_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 16), command=clear_entry).grid(row=row_val, column=0, columnspan=2, padx=5, pady=5)
tk.Button(root, text='DEL', padx=20, pady=20, font=('Arial', 16), command=delete_last).grid(row=row_val, column=2, columnspan=2, padx=5, pady=5)

root.mainloop()

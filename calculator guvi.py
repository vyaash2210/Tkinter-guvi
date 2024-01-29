import tkinter as tk

def press_key(value):
    entry_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, entry_text + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Creating main window
root = tk.Tk()
root.title("Calculator")

# Entry widget to display input and results
entry = tk.Entry(root, width=20, font=('Arial', 14), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

# Creating buttons and add them to the grid
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
              command=lambda button=button: press_key(button) if button != '=' else calculate_result()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Starting the Tkinter event loop
root.mainloop()

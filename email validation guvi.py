import tkinter as tk
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def submit_form():
    email_value = entry_email.get()
    
    if validate_email(email_value):
        result_label.config(text="Form submitted successfully!")
    else:
        result_label.config(text="Form failed to submit. Invalid email.")

root = tk.Tk()
root.title("Form Validation")

entry_email = tk.Entry(root, width=30, font=('Arial', 12))
entry_email.grid(row=0, column=0, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=0, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="", font=('Arial', 12))
result_label.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()

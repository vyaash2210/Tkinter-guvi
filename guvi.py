import tkinter as tk

def create_gui_with_buttons():
    def start():
        print("Start Button Pressed")

    def stop():
        print("Stop Button Pressed")

    def reset():
        print("Reset Button Pressed")

    # Creating main window
    root = tk.Tk()
    root.title("Button GUI")

    # Creating buttons
    start_button = tk.Button(root, text="Start", command=start)
    stop_button = tk.Button(root, text="Stop", command=stop)
    reset_button = tk.Button(root, text="Reset", command=reset)

    # Arranging buttons in a grid
    start_button.grid(row=0, column=0)
    stop_button.grid(row=0, column=1)
    reset_button.grid(row=0, column=2)

    # Starting the Tkinter event loop
    root.mainloop()

# Calling the function to create GUI with buttons
create_gui_with_buttons()

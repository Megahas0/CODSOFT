import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x605")
display = tk.StringVar()
display.set("0")
display_entry = tk.Entry(root, textvariable=display, justify="right", font=("Arial", 24))
display_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

def update_display(value):
    current_text = display.get()
    if current_text == "0" and value != ".":
        display.set(value)
    else:
        display.set(current_text + value)

def clear_display():
    display.set("0")

def calculate():
    try:
        expression = display.get()
        result = str(eval(expression))
        display.set(result)
    except Exception:
        display.set("Error")

row, col = 1, 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, command=calculate,
                  height=3, width=6, font=("Arial", 16)).grid(row=row, column=col, padx=10, pady=10)
    elif button == "C":
        tk.Button(root, text=button, command=clear_display,
                  height=3, width=6, font=("Arial", 16)).grid(row=row, column=col, padx=10, pady=10)
    else:
        tk.Button(root, text=button, command=lambda b=button: update_display(b),
                  height=3, width=6, font=("Arial", 16)).grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()

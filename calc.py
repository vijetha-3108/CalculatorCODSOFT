import tkinter as tk
import math

def on_click(value):
    # Evaluate the '=' button (Calculate the expression)
    if value == "=":
        try:
            result = eval(entry_var.get())
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    
    # Clear all inputs when 'C' button is pressed
    elif value == "C":
        entry_var.set("")
    
    # Calculate factorial when '!' button is pressed
    elif value == "!":
        try:
            current_value = int(entry_var.get())
            if current_value >= 0:
                entry_var.set(str(math.factorial(current_value)))
            else:
                entry_var.set("Error")
        except ValueError:
            entry_var.set("Error")
    
    # Delete the last character when '⌫' button is pressed
    elif value == "⌫":
        entry_var.set(entry_var.get()[:-1])
    
    # Change the sign of the number when '+/-' is pressed
    elif value == "+/-":
        if entry_var.get():
            entry_var.set(str(-float(entry_var.get())))
    
    # Calculate the reciprocal (1/x) when '1/x' button is pressed
    elif value == "1/x":
        try:
            current_value = float(entry_var.get())
            if current_value != 0:
                entry_var.set(str(1 / current_value))
            else:
                entry_var.set("Error")
        except ValueError:
            entry_var.set("Error")
    
    # Calculate the square of the number (x²) when 'x²' button is pressed
    elif value == "x²":
        try:
            current_value = float(entry_var.get())
            entry_var.set(str(current_value ** 2))
        except ValueError:
            entry_var.set("Error")
    
    # Calculate the square root (√x) when '√x' button is pressed
    elif value == "√x":
        try:
            current_value = float(entry_var.get())
            if current_value >= 0:
                entry_var.set(str(math.sqrt(current_value)))
            else:
                entry_var.set("Error")
        except ValueError:
            entry_var.set("Error")
    
    # If it's a regular number or operator, just append it to the entry field
    else:
        entry_var.set(entry_var.get() + value)


# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)
root.configure(bg='black')

# Create a StringVar to hold the value entered in the entry field
entry_var = tk.StringVar()

# Create the entry field for displaying input and results
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), justify='right', bg='black', fg='white', insertbackground='white')
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, padx=10, pady=10)

# Define the layout of buttons in the calculator
buttons = [
    ["%", "!", "C", "⌫"],  
    ["1/x", "x²", "√x", "/"],  
    ["7", "8", "9", "*"], 
    ["4", "5", "6", "-"],  
    ["1", "2", "3", "+"],  
    ["+/-", "0", ".", "="]  
]

# Create a frame to contain the buttons
frame = tk.Frame(root, bg="black")
frame.pack(fill=tk.BOTH, expand=True)

# Function to create buttons and place them in the layout
def create_button(btn, row_frame):
    button = tk.Button(row_frame, text=btn, command=lambda b=btn: on_click(b),
                       font=("Arial", 12), bg="black", fg="white", 
                       activebackground="gray", activeforeground="white",
                       relief=tk.FLAT, height=2)
    button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=2)
    button.bind("<Enter>", lambda e, btn=button: btn.config(bg="gray"))
    button.bind("<Leave>", lambda e, btn=button: btn.config(bg="black"))

# Create rows of buttons
for row in buttons:
    row_frame = tk.Frame(frame, bg="black")
    row_frame.pack(fill=tk.BOTH, expand=True)
    for btn in row:
        create_button(btn, row_frame)

def on_key(event):
    key = event.keysym
    if key.isdigit() or key in ["plus", "minus", "asterisk", "slash", "Return", "BackSpace", "Escape", "period"]:
        key_map = {
            "plus": "+", "minus": "-", "asterisk": "*", "slash": "/",
            "Return": "=", "BackSpace": "⌫", "Escape": "C", "period": "."
        }
        on_click(key_map.get(key, key))

root.bind("<Key>", on_key)

root.update_idletasks()
root.geometry(f"300x{root.winfo_height()}")

# Start the application loop
root.mainloop()

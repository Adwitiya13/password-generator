import tkinter as tk
import random
import string

def generate_password(length):
    if length < 1:
        return "Length must be greater than 0"
    
    # Define the character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate():
    try:
        length = int(entry_length.get())
        if length < 1:
            result_var.set("Length must be greater than 0")
        else:
            password = generate_password(length)
            result_var.set(password)
    except ValueError:
        result_var.set("Invalid input. Please enter a number.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg='red')

# Create and place widgets
tk.Label(root, text="Enter password length:", bg='red', fg='white').grid(row=0, column=0, padx=10, pady=10)
entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Generate Password", command=on_generate).grid(row=1, column=0, columnspan=2, padx=10, pady=10)

tk.Label(root, text="Generated Password:", bg='red', fg='white').grid(row=2, column=0, padx=10, pady=10)
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, state='readonly').grid(row=2, column=1, padx=10, pady=10)

# Run the main event loop
root.mainloop()

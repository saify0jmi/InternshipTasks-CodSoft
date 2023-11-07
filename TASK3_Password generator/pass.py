import itertools as it
import random
import pyperclip
import tkinter as tk
from tkinter import ttk

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def gen_pass(n, c_type):
    characters = {
        "Uppercases": 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        "Lowercases": 'abcdefghijklmnopqrstuvwxyz',
        "Numbers": '0123456789',
        "Symbols": '!@#$&*?_-',
    }

    s_comb_l = list(c_type)  # selected character combination list
    c_per_pass = n // len(s_comb_l)
    extra_c = n - (c_per_pass * len(s_comb_l))
    password_l = []
    all_char = []

    for element in s_comb_l:
        z = characters[element]
        l = [char for char in z]
        all_char.extend(l)
        c = random.choices(l, k=c_per_pass)
        password_l.extend(c)

    e_c = random.choices(all_char, k=extra_c)
    password_l.extend(e_c)
    random.shuffle(password_l)
    password = "".join(password_l)
    return password


def generate_password():
    n = int(length_entry.get())
    selected_combinations_str = combinations_combobox.get()
    selected_combinations = [item.strip() for item in selected_combinations_str.split(',')]
    password = gen_pass(n, selected_combinations)
    result_label.config(text="Your password: " + password)
    pyperclip.copy(password)


# Create a Tkinter window
window = tk.Tk()
window.title("Password Generator")

# Create a label for the length of the password
length_label = tk.Label(window, text="Length of Password:")
length_label.pack()

# Create an entry field for entering the password length
length_entry = tk.Entry(window)
length_entry.pack()

# Create a label for selecting character combinations
combinations_label = tk.Label(window, text="Select Character Combinations:")
combinations_label.pack()

# Create a Combobox for selecting character combinations
combinations_combobox = ttk.Combobox(window, values=[
    "Numbers",
    "Uppercases",
    "Lowercases",
    "Symbols",
    "Numbers, Uppercases",
    "Numbers, Lowercases",
    "Numbers, Symbols",
    "Uppercases, Lowercases",
    "Uppercases, Symbols",
    "Lowercases, Symbols",
    "Numbers, Uppercases, Lowercases",
    "Numbers, Uppercases, Symbols",
    "Numbers, Lowercases, Symbols",
    "Uppercases, Lowercases, Symbols",
    "Numbers, Uppercases, Lowercases, Symbols"
])

combinations_combobox.pack()
combinations_combobox.set(("Numbers",))

# Create a button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Create a label for displaying the generated password
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()

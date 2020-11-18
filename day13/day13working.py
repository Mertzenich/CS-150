#!/usr/bin/env python3

import tkinter as tk
import os
from tkinter import ttk, messagebox, simpledialog, filedialog


window = tk.Tk()

answer = messagebox.askokcancel('Question', "Do you want to repeat?")
answer = messagebox.askquestion('Question', 'Yes or no?')

label = ttk.Label(window, text='Hello world!')
label.grid(row=1, column=2)
# label.pack()

window.mainloop()

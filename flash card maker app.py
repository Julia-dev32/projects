import tkinter as tk
from tkinter import ttk
import requests

button_pressed = False

def add_flashcard(entry_widget, flashcard_shape):
    global button_pressed
    if button_pressed == True:
        flashcard_text = entry_widget.get()
        button_pressed = False

def add_button_clicked(entry_widget):
    global button_pressed
    button_pressed = True
    add_flashcard(entry_widget)

def ui_setup():
    root= tk.Tk()
    root.title("Flashcard app")
    root.geometry=(400, 500)
    root.configure(bg="white")


    flashcard_entry = tk.Entry(root, font=("Arial", 16), text="Enter text", width=30)
    flashcard_entry.pack(pady=20)
     
    canvas = tk.Canvas(root, bg="White", highlightthickness=1)
    scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
    flashcard_shape = tk.Frame(canvas, bg="white")

    flashcard_shape.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0,0), window=flashcard_shape, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True, pady=10, padx=10)
    scrollbar.pack(side="right", fill="y")
    add_button = tk.Button(root, text="Add flash card", font=("Arial", 16), command=lambda: add_button_clicked(flashcard_shape))
    add_button.pack(pady=10)

    root.mainloop()


ui_setup()
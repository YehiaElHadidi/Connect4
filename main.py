import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import pyautogui
import time
import game


class MainGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Main GUI")
        self.master.geometry("500x400")

        self.title_label = tk.Label(
            self.master, text="Connect Four AI", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.image_frame = tk.Frame(self.master)
        self.image_frame.pack(pady=30)

        self.image = Image.open("connect4.png")
        self.image = self.image.resize((200, 200))
        self.photo = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(self.image_frame, image=self.photo)
        self.image_label.pack()

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack()


        self.button1 = tk.Button(self.button_frame, text="Choose Algorithm", font=(
            "Arial", 12), command=self.open_subgui)
        self.button1.pack(padx=10, pady=10)

    def open_subgui(self):
        sub_gui = tk.Toplevel(self.master)
        SubGUI(sub_gui)


class SubGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x300")

        self.master.title("Choose an Algorithm")
        self.menu = tk.Menu(self.master, font=("Arial", 12))
        self.master.config(menu=self.menu)

        self.selected_algorithm = tk.StringVar()
        self.selected_algorithm.set("Choose an algorithm")
        self.options_menu = tk.Menu(
            self.menu, tearoff=0, font=("Arial", 12), borderwidth=25)
        self.menu.add_cascade(label="Choose an algorithm",
                              menu=self.options_menu)
        self.options_menu.add_command(
            label="Minimax", command=lambda: self.select_algorithm("Minimax"))
        self.options_menu.add_command(
            label="Alpha beta pruning", command=lambda: self.select_algorithm("Alpha beta pruning"))

        self.label = tk.Label(
            self.master, text="Select an algorithm:", font=("Arial", 12))
        self.label.pack(pady=(15, 10))

        self.radio_frame = tk.Frame(self.master)
        self.radio_frame.pack(pady=10, padx=20)

        self.radio1 = tk.Radiobutton(self.radio_frame, text="Minimax", font=(
            "Arial", 12), variable=self.selected_algorithm, value="Minimax")
        self.radio2 = tk.Radiobutton(self.radio_frame, text="Alpha beta pruning", font=(
            "Arial", 12), variable=self.selected_algorithm, value="Alpha beta pruning")

        self.radio1.pack(padx=10, pady=5, anchor=tk.W)
        self.radio2.pack(padx=10, pady=5, anchor=tk.W)

        self.selected_difficulty = tk.StringVar()
        self.selected_difficulty.set("Easy")

        # Create the drop-down list for difficulty level
        self.difficulty_label = tk.Label(
            self.master, text="Select difficulty:", font=("Arial", 12))
        self.difficulty_label.pack(pady=10)

        self.difficulty_dropdown = ttk.Combobox(
            self.master, textvariable=self.selected_difficulty)
        self.difficulty_dropdown['values'] = ('Easy', 'Medium', 'Hard')
        self.difficulty_dropdown.pack(pady=10)

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10)

        self.button2 = tk.Button(self.button_frame, text="START", font=(
            "Arial", 12), command=self.open_website)
        self.button2.pack(padx=10)

    def select_algorithm(self, algorithm):
        self.selected_algorithm.set(algorithm)

    def depth_calculation(self):
        if self.selected_difficulty.get() == 'Easy':
            return 2
        if self.selected_difficulty.get() == 'Medium':
            return 4
        if self.selected_difficulty.get() == 'Hard':
            return 6

    def open_website(self):
        selected_algorithm = self.selected_algorithm.get()
        depth = self.depth_calculation()
        print(f"Selected algorithm: {selected_algorithm}, depth: {depth}")
        webbrowser.open_new("http://kevinshannon.com/connect4/")
        game.main(self.selected_algorithm.get(), depth)


if __name__ == "__main__":
    root = tk.Tk()
    MainGUI(root)
    root.mainloop()

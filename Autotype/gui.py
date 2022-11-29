import tkinter as tk
from .core import Autotype
import customtkinter
from tkinter import filedialog
import tkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"


class App(customtkinter.CTk):

    WIDTH = 780
    HEIGHT = 520

    def __init__(self):
        super().__init__()
        self.resizable(0, 0)
        self.title("Autotype")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # ============ created two frames ============

        # configured grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(
            master=self, width=180, corner_radius=0
        )
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(
            0, minsize=10
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(
            8, minsize=20
        )  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(
            11, minsize=10
        )  # empty row with minsize as spacing

        self.delay = customtkinter.CTkEntry(
            master=self.frame_left, width=140, placeholder_text="Enter time delay"
        )
        self.delay.grid(row=1, column=0, pady=20, padx=20)

        self.button_2 = customtkinter.CTkButton(
            master=self.frame_left,
            text="Start Typing",
            fg_color=("gray75", "gray30"),  # <- custom tuple-color
            command=self.start_typing,
            hover=True,
        )
        self.button_2.grid(row=3, column=0, pady=10, padx=20)

        self.label = customtkinter.CTkLabel(master=self.frame_left, text="")
        self.label.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.switch_1 = customtkinter.CTkSwitch(
            master=self.frame_left, text="Dark Mode", command=self.change_mode
        )
        self.switch_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        self.code = customtkinter.CTkTextbox(
            master=self.frame_right, width=520, height=400
        )
        self.code.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.label_2 = customtkinter.CTkLabel(
            master=self.frame_right,
            text="Enter Your Code",
            text_font=("Roboto Medium", -16),
        )  # font name and size in px
        self.label_2.grid(row=8, column=0, columnspan=2, pady=20, padx=20, sticky="we")
        self.label_2.place(relx=0.38, rely=0.92)

    def open_file(self):
        filePath = filedialog.askopenfile()
        return filePath.name

    def start_typing(self):
        delay = self.delay.get()
        code = self.code.textbox.get("1.0", tk.END)
        if str(code).isspace() and delay != "":  # when code is not provided
            Autotype.type(path=self.open_file(), delay=int(delay), code=None)
            self.label.configure(text="Done Writing Script")
        elif str(code).isspace() and delay == "":
            Autotype.type(path=self.open_file(), delay=int(delay), code=None)
            self.label.configure(text="Done Writing Script")
        elif not str(code).isspace() and delay != "":  # when code is provided
            Autotype.type(path=None, delay=int(delay), code=code)
            self.label.configure(text="Done Writing Script")
        else:
            Autotype.type(path=None, delay=int(delay), code=code)
            self.label.configure(text="Done Writing Script")

    def change_mode(self):
        if self.switch_1.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()
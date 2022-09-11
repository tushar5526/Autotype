# Imports
import sys

if sys.version_info[0] == 3:
    import tkinter as tk
    from tkinter import filedialog
else:
    import Tkinter as tk
    from TKinter import filedialog
from Simulator import Type
from PIL import ImageTk, Image

# GUI using Tkinter

# Root Widget
root_widget = tk.Tk()
root_widget.title("KeyBoard Simulator")

# Width and Height
root_widget.geometry("780x480")

# Image
frame = tk.Frame(root_widget, width=600, height=400)
frame.pack()
frame.place(anchor="center", relx=0.5, rely=0.5)
body_image = ImageTk.PhotoImage(Image.open("gui_assets/type.jpg"))
label_for_body_image = tk.Label(frame, image=body_image)
label_for_body_image.pack()

# Labeling the window title
root_window_title = tk.Label(
    root_widget, text="AutoType 🖊", fg="#8FBDD3", font=("", 62)
)
root_window_title.pack()

# Input Box for Time Delay
entry_for_time_delay = tk.Entry(root_widget, borderwidth=5)
entry_for_time_delay.pack()
entry_for_time_delay.insert(0, 3)


# Logic
# Function for Addition of Time Delay
def add_time_delay():
    mylable_time = tk.Label(
        root_widget, text=f"Time Delay of {entry_for_time_delay.get()} seconds added"
    )
    mylable_time.pack()


# Function for Opening File
def open_file():
    filePath = filedialog.askopenfile()
    return filePath.name


# Function for Writing File through keyboard
def file_writer():
    Type(path=open_file(), delay=int(entry_for_time_delay.get()))
    done_task = tk.Label(text="Done Writing Script")
    done_task.pack()


# Button widget instance
button_for_add_time_delay = tk.Button(
    root_widget,
    text="Add time Delay in Seconds",
    activebackground="#345",
    activeforeground="white",
    padx=5,
    pady=5,
    command=add_time_delay,
)
button_for_add_time_delay.pack()

# Button widget instance
button_for_writing_file = tk.Button(
    root_widget,
    text="Write File",
    activebackground="#345",
    activeforeground="white",
    padx=5,
    pady=5,
    command=file_writer,
)
button_for_writing_file.pack()

root_widget.mainloop()

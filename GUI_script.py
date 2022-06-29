# Imports
import sys

if sys.version_info[0] == 3:
    import tkinter as tk
    from tkinter import filedialog
else:
    import Tkinter as tk
    from TKinter import filedialog
from Simulator.simulate_keyboard import Type
from PIL import ImageTk, Image

# GUI using TKinter

# Root Widget
root = tk.Tk()
root.title("KeyBoard Simulator")

# Width and Height
root.geometry('780x480')

# Image
frame = tk.Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)
body_image = ImageTk.PhotoImage(Image.open('gui_assets/type.jpg'))
label = tk.Label(frame, image=body_image)
label.pack()

# Labeling the window
Title = tk.Label(root, text="AutoType 🖊", fg="#8FBDD3", font=('', 62))
Title.pack()

# Input Box for Time Delay
entry1 = tk.Entry(root, borderwidth=5)
entry1.pack()
entry1.insert(0, 3)


# Logic
def add_time_delay():
    mylable_time = tk.Label(root, text=f"Time Delay of {entry1.get()} seconds added")
    mylable_time.pack()


# Function for Opening File
def open_file():
    filePath = filedialog.askopenfile()
    return filePath.name


# Function for Writing File
def writer():
    Type(path=open_file(), delay=int(entry1.get()))
    done_task = tk.Label(text="Done Writing Script")
    done_task.pack()


# Button widget instance
btn0 = tk.Button(root, text="Add time Delay in Seconds", activebackground='#345', activeforeground='white', padx=5,
                 pady=5, command=add_time_delay)
btn0.pack()

# Button widget instance
btn1 = tk.Button(root, text="Write File", activebackground='#345', activeforeground='white', padx=5, pady=5,
                 command=writer)
btn1.pack()

root.mainloop()

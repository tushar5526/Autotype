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



# Function for Opening File
def open_file():
    filePath = filedialog.askopenfile()
    return filePath.name

# Function for Writing File
def writer():
    Type(path=open_file(),delay=3)
    done_task = tk.Label(text="Done Writting Script")
    done_task.pack()



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
label = tk.Label(frame, image = body_image)
label.pack()


# Labeling the window
Title = tk.Label(root, text="AutoType 🖊", fg="#8FBDD3", font=('',62))
Title.pack()

# Button widget instance
btn1 = tk.Button(root, text="Write File", activebackground='#345',activeforeground='white', padx=5, pady=5, command=writer )
btn1.pack()

root.mainloop()
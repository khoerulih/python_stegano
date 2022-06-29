from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb
import enum

root = Tk()
root.title("UAS Stegano Kelompok 2")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg='#5B1C6A')


class SIZE_UNIT(enum.Enum):
    BYTES = 1
    KB = 2
    MB = 3
    GB = 4


image_size = 0


def convert_unit(size_in_bytes, unit):
    """ Convert the size from bytes to other units like KB, MB or GB"""
    if unit == SIZE_UNIT.KB:
        return size_in_bytes/1024
    elif unit == SIZE_UNIT.MB:
        return size_in_bytes/(1024*1024)
    elif unit == SIZE_UNIT.GB:
        return size_in_bytes/(1024*1024*1024)
    else:
        return size_in_bytes


def get_file_size(file_name, size_type=SIZE_UNIT.BYTES):
    """ Get file in size in given unit like KB, MB or GB"""
    size = os.path.getsize(file_name)
    return round(convert_unit(size, size_type), 2)


def showimage():
    global filename
    global image_size
    global showDynamicUi
    filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetype=(
        ("PNG file", "*.png"), ("JPG file", "*.jpg"), ("All file", "*.txt")))
    img = Image.open(filename)
    img = ImageTk.PhotoImage(img)
    image_size = get_file_size(filename, SIZE_UNIT.KB)
    showDynamicUi()
    lbl.configure(image=img, width=250, height=250)
    lbl.image = img


def hidemessage():
    global secret
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)
    text1.delete('1.0', END)


def save():
    secret.save("result.png")


def showmessage():
    clear_message = lsb.reveal(filename)
    text1.delete(1.0, END)
    text1.insert(END, clear_message)


def showDynamicUi():
    Label(root, text="Ukuran Gambar: {} Kb".format(image_size), bg="#5B1C6A", fg="white",
          font="arial 14 bold", width=50, anchor="w").place(x=100, y=50)


# logo
logo = PhotoImage(file="logo.png")
Label(root, image=logo, bg="#5B1C6A", width=64, height=64).place(x=10, y=0)

Label(root, text=f"Stegano Kelompok 2", bg="#5B1C6A",
      fg="white", font="arial 18 bold").place(x=100, y=10)

showDynamicUi()

# First Frame
f = Frame(root, bd=3, bg="white", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="white")
lbl.place(x=40, y=10)

# Second Frame
frame2 = Frame(root, bd=3, width=340, height=280, bg="#9A56A6", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Roboto 16", bg="#EED1E8",
             fg="#6A206F", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# Third Frame
frame3 = Frame(root, bd=1, bg="#67247D", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2,
       font="arial 14 bold", bg="#512375", fg="white", command=showimage).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2,
       font="arial 14 bold", bg="#512375", fg="white", command=save).place(x=180, y=30)
Label(frame3, text="Save or Open Image",
      bg="#67247D", fg="white").place(x=20, y=5)

# Fourth Frame
frame4 = Frame(root, bd=3, bg="#67247D", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide", width=10, height=2,
       font="arial 14 bold", bg="#512375", fg="white", command=hidemessage).place(x=20, y=30)
Button(frame4, text="Show", bg="#512375", fg="white", width=10, height=2,
       font="arial 14 bold", command=showmessage).place(x=180, y=30)
Label(frame4, text="Hide or Show Message",
      bg="#67247D", fg="white").place(x=20, y=5)

root.mainloop()

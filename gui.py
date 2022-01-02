
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import string
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# Stopoffsets 
OFFSET_1 = 0
OFFSET_2 = 200
OFFSET_3 = 480
OFFSET_4 = 800


str_angle = str()
set_angle = float()
stop_offset = float()
stop_value = float()


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1440x1024")
window.configure(bg = "#FFFFFF")

def add_digit_to_angle(value):
    global str_angle

    if value == 'C':
        str_angle = str()
        canvas.itemconfig(set_angle, text=''.join([str_angle,'°']))
        return

    if value == 'Enter':
        change_angle(str_angle)
        str_angle = str()
        return

    str_angle = str_angle + value
    canvas.itemconfig(set_angle, text=''.join([str_angle,'°']))


def change_angle(angle):
    global fl_angle
    try:
        result = eval(angle)
        print(result)
        canvas.itemconfig(set_angle, text=''.join([str(result),'°']))
        fl_angle = float(result)


    except Exception as e:
        print(e)
        canvas.itemconfig(set_angle, text='Error')

def change_selected_button(button):
    button_3["bg"]="white"
    button_4["bg"]="white"
    button_5["bg"]="white"
    button_6["bg"]="white"
    button["bg"]="grey"
    return

def change_stop_offset(value):
    global stop_offset

    if value == 1:
        stop_offset = OFFSET_1
        change_selected_button(button_6)
    elif value == 2:
        stop_offset = OFFSET_2
        change_selected_button(button_5)
    elif value == 3:
        stop_offset = OFFSET_3
        change_selected_button(button_4)
    elif value == 4:
        stop_offset = OFFSET_4
        change_selected_button(button_3)
    str_offset= str(stop_offset)
    print(''.join(["Aktueller Anschlagoffset: ",str_offset]))
    display_leng_stop()
    return

def display_leng_stop():
    canvas.itemconfig(leng_stop, text=''.join([str(stop_value+stop_offset),' mm']))


#--------------- create GUI items ------------------

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=501.0,
    y=751.0,
    width=323.0,
    height=140.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=55.0,
    y=751.0,
    width=323.0,
    height=140.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    bg = "#FFFFFF",
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_stop_offset(4),
    relief="flat",
)
button_3.place(
    x=714.0,
    y=600.0,
    width=120.0,
    height=120.0
)


button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    bg = "#FFFFFF",
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_stop_offset(3),
    relief="flat",

)
button_4.place(
    x=491.0,
    y=600.0,
    width=120.0,
    height=120.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    bg = "#FFFFFF",
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_stop_offset(2),
    relief="flat"
)
button_5.place(
    x=268.0,
    y=600.0,
    width=120.0,
    height=120.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    bg = "grey",
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: change_stop_offset(1),
    relief="flat"
)
button_6.place(
    x=45.0,
    y=600.0,
    width=120.0,
    height=120.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('Enter'),
    relief="flat"
)
button_7.place(
    x=907.0,
    y=751.0,
    width=474.0,
    height=140.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('0'),
    relief="flat"
)
button_8.place(
    x=907.0,
    y=590.0,
    width=140.0,
    height=140.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('.'),
    relief="flat"
)
button_9.place(
    x=1074.0,
    y=590.0,
    width=140.0,
    height=140.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('C'),
    relief="flat"
)
button_10.place(
    x=1241.0,
    y=590.0,
    width=140.0,
    height=140.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('7'),
    relief="flat"
)
button_11.place(
    x=907.0,
    y=424.0,
    width=140.0,
    height=140.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('8'),
    relief="flat"
)
button_12.place(
    x=1074.0,
    y=424.0,
    width=140.0,
    height=140.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('9'),
    relief="flat"
)
button_13.place(
    x=1241.0,
    y=424.0,
    width=140.0,
    height=140.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('4'),
    relief="flat"
)
button_14.place(
    x=907.0,
    y=257.0,
    width=140.0,
    height=140.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('5'),
    relief="flat"
)
button_15.place(
    x=1074.0,
    y=257.0,
    width=140.0,
    height=140.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('6'),
    relief="flat"
)
button_16.place(
    x=1241.0,
    y=257.0,
    width=140.0,
    height=140.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('3'),
    relief="flat"
)
button_17.place(
    x=1241.0,
    y=90.0,
    width=140.0,
    height=140.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('2'),
    relief="flat"
)
button_18.place(
    x=1074.0,
    y=90.0,
    width=140.0,
    height=140.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: add_digit_to_angle('1'),
    relief="flat"
)
button_19.place(
    x=907.0,
    y=90.0,
    width=140.0,
    height=140.0
)

canvas.create_rectangle(
    396.0,
    423.0,
    824.0,
    563.0,
    fill="#C4C4C4",
    outline="")

leng_stop=canvas.create_text(
    610.0,
    494.0,
    anchor="center",
    text="0.0 mm",
    fill="#000000",
    font=("Roboto", 72 * -1)
)

canvas.create_text(
    55.0,
    494.0,
    anchor="w",
    text="Anschlag:",
    fill="#000000",
    font=("Roboto", 72 * -1)
)

canvas.create_rectangle(
    396.0,
    256.0,
    824.0,
    396.0,
    fill="#C4C4C4",
    outline="")

current_angle=canvas.create_text(
    610.0,
    326.0,
    anchor="center",
    text="90°",
    fill="#000000",
    font=("Roboto", 72 * -1)
)

canvas.create_text(
    55.0,
    327.0,
    anchor="w",
    text="Ist:",
    fill="#000000",
    font=("Roboto", 72 * -1)
)

canvas.create_rectangle(
    396.0,
    90.0,
    824.0,
    230.0,
    fill="#C4C4C4",
    outline="")

set_angle =canvas.create_text(
    610.0,
    160.0,
    anchor="center",
    text="90°",
    fill="#000000",
    font=("Roboto", 72 * -1)
)

canvas.create_text(
    55.0,
    160.0,
    anchor="w",
    text="Soll:",
    fill="#000000",
    font=("Roboto", 72 * -1)
)

# -------------------- Start Mainloop --------------------

window.resizable(True, True)
window.mainloop()

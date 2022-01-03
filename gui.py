
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import configparser
import threading
import queue
import time
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter
from tkinter.constants import DISABLED


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

# Stop offsets 
OFFSET_1 = 0
OFFSET_2 = 200
OFFSET_3 = 480
OFFSET_4 = 800


class GUI():

    def __init__(self,parent):
        self.str_angle = str()
        self.stop_offset = float()
        self.stop_value = float()
        self.fl_set_angle = float()
        self.fl_current_angle = float()
        self.config = configparser.ConfigParser()
        self.window = parent    
        self.config.read('Settings.INI')
        self.running = True
        # self.fl_set_angle = float(config['DEFAULT']['SetAngle'])

        #--------------- create GUI items ------------------

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.stop_bending(),
            relief="flat"
        )
        self.button_1.place(
            x=501.0,
            y=751.0,
            width=323.0,
            height=140.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.start_bending(),
            relief="flat"
        )
        self.button_2.place(
            x=55.0,
            y=751.0,
            width=323.0,
            height=140.0
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(
            bg = "#FFFFFF",
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_stop_offset(4),
            relief="flat",
        )
        self.button_3.place(
            x=714.0,
            y=600.0,
            width=120.0,
            height=120.0
        )


        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(
            bg = "#FFFFFF",
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_stop_offset(3),
            relief="flat",

        )
        self.button_4.place(
            x=491.0,
            y=600.0,
            width=120.0,
            height=120.0
        )

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(
            bg = "#FFFFFF",
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_stop_offset(2),
            relief="flat"
        )
        self.button_5.place(
            x=268.0,
            y=600.0,
            width=120.0,
            height=120.0
        )

        self.button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(
            bg = "grey",
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_stop_offset(1),
            relief="flat"
        )
        self.button_6.place(
            x=45.0,
            y=600.0,
            width=120.0,
            height=120.0
        )

        self.button_image_7 = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('Enter'),
            relief="flat"
        )
        self.button_7.place(
            x=907.0,
            y=751.0,
            width=474.0,
            height=140.0
        )

        self.button_image_8 = PhotoImage(
            file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('0'),
            relief="flat"
        )
        self.button_8.place(
            x=907.0,
            y=590.0,
            width=140.0,
            height=140.0
        )

        self.button_image_9 = PhotoImage(
            file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('.'),
            relief="flat"
        )
        self.button_9.place(
            x=1074.0,
            y=590.0,
            width=140.0,
            height=140.0
        )

        self.button_image_10 = PhotoImage(
            file=self.relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('C'),
            relief="flat"
        )
        self.button_10.place(
            x=1241.0,
            y=590.0,
            width=140.0,
            height=140.0
        )

        self.button_image_11 = PhotoImage(
            file=self.relative_to_assets("button_11.png"))
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('7'),
            relief="flat"
        )
        self.button_11.place(
            x=907.0,
            y=424.0,
            width=140.0,
            height=140.0
        )

        self.button_image_12 = PhotoImage(
            file=self.relative_to_assets("button_12.png"))
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('8'),
            relief="flat"
        )
        self.button_12.place(
            x=1074.0,
            y=424.0,
            width=140.0,
            height=140.0
        )

        self.button_image_13 = PhotoImage(
            file=self.relative_to_assets("button_13.png"))
        self.button_13 = Button(
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('9'),
            relief="flat"
        )
        self.button_13.place(
            x=1241.0,
            y=424.0,
            width=140.0,
            height=140.0
        )

        self.button_image_14 = PhotoImage(
            file=self.relative_to_assets("button_14.png"))
        self.button_14 = Button(
            image=self.button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('4'),
            relief="flat"
        )
        self.button_14.place(
            x=907.0,
            y=257.0,
            width=140.0,
            height=140.0
        )

        self.button_image_15 = PhotoImage(
            file=self.relative_to_assets("button_15.png"))
        self.button_15 = Button(
            image=self.button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('5'),
            relief="flat"
        )
        self.button_15.place(
            x=1074.0,
            y=257.0,
            width=140.0,
            height=140.0
        )

        self.button_image_16 = PhotoImage(
            file=self.relative_to_assets("button_16.png"))
        self.button_16 = Button(
            image=self.button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('6'),
            relief="flat"
        )
        self.button_16.place(
            x=1241.0,
            y=257.0,
            width=140.0,
            height=140.0
        )

        self.button_image_17 = PhotoImage(
            file=self.relative_to_assets("button_17.png"))
        self.button_17 = Button(
            image=self.button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('3'),
            relief="flat"
        )
        self.button_17.place(
            x=1241.0,
            y=90.0,
            width=140.0,
            height=140.0
        )

        self.button_image_18 = PhotoImage(
            file=self.relative_to_assets("button_18.png"))
        self.button_18 = Button(
            image=self.button_image_18,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('2'),
            relief="flat"
        )
        self.button_18.place(
            x=1074.0,
            y=90.0,
            width=140.0,
            height=140.0
        )

        self.button_image_19 = PhotoImage(
            file=self.relative_to_assets("button_19.png"))
        self.button_19 = Button(
            image=self.button_image_19,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('1'),
            relief="flat"
        )
        self.button_19.place(
            x=907.0,
            y=90.0,
            width=140.0,
            height=140.0
        )

        self.canvas.create_rectangle(
            396.0,
            423.0,
            824.0,
            563.0,
            fill="#C4C4C4",
            outline="")

        self.leng_stop = self.canvas.create_text(
            610.0,
            494.0,
            anchor="center",
            text="0.0 mm",
            fill="#000000",
            font=("Roboto", 72 * -1)
        )

        self.canvas.create_text(
            55.0,
            494.0,
            anchor="w",
            text="Anschlag:",
            fill="#000000",
            font=("Roboto", 72 * -1)
        )

        self.canvas.create_rectangle(
            396.0,
            256.0,
            824.0,
            396.0,
            fill="#C4C4C4",
            outline="")

        self.current_angle = self.canvas.create_text(
            610.0,
            326.0,
            anchor="center",
            text="90°",
            fill="#000000",
            font=("Roboto", 72 * -1)
        )

        self.canvas.create_text(
            55.0,
            327.0,
            anchor="w",
            text="Ist:",
            fill="#000000",
            font=("Roboto", 72 * -1)
        )

        self.canvas.create_rectangle(
            396.0,
            90.0,
            824.0,
            230.0,
            fill="#C4C4C4",
            outline="")

        self.set_angle = self.canvas.create_text(
            610.0,
            160.0,
            anchor="center",
            text="0°",
            fill="#000000",
            font=("Roboto", 72 * -1)
        )

        self.canvas.create_text(
            55.0,
            160.0,
            anchor="w",
            text="Soll:",
            fill="#000000",
            font=("Roboto", 72 * -1)
        )

    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)


    def add_digit_to_angle(self, value):

        if value == 'C':
            self.str_angle = str()
            self.canvas.itemconfig(self.set_angle, text=''.join([self.str_angle,'°']))
            return

        if value == 'Enter':
            self.change_angle(self.str_angle)
            self.str_angle = str()
            return

        self.str_angle = self.str_angle + value
        self.canvas.itemconfig(self.set_angle, text=''.join([self.str_angle,'°']))


    def change_angle(self, angle):
        try:
            self.result = eval(angle)
            print(self.result)
            self.canvas.itemconfig(self.set_angle, text=''.join([str(self.result),'°']))
            self.fl_set_angle = float(self.result)
            # config['DEFAULT']['SetAngle'] = str(result)
            # with open('Settings.INI', 'w') as configfile:    # save to configfile
            #     config.write(configfile)

        except Exception as e:
            print(e)
            self.canvas.itemconfig(self.set_angle, text='Error')

    def change_selected_button(self, button):
        self.button_3["bg"]="white"
        self.button_4["bg"]="white"
        self.button_5["bg"]="white"
        self.button_6["bg"]="white"
        button["bg"]="grey"
        return

    def change_stop_offset(self, value):
        if value == 1:
            self.stop_offset = OFFSET_1
            self.change_selected_button(self.button_6)
        elif value == 2:
            self.stop_offset = OFFSET_2
            self.change_selected_button(self.button_5)
        elif value == 3:
            self.stop_offset = OFFSET_3
            self.change_selected_button(self.button_4)
        elif value == 4:
            self.stop_offset = OFFSET_4
            self.change_selected_button(self.button_3)
        str_offset= str(self.stop_offset)
        print(''.join(["Aktueller Anschlagoffset: ", str_offset]))
        self.display_leng_stop()
        return

    def display_leng_stop(self):
        self.canvas.itemconfig(self.leng_stop, text=''.join([str(self.stop_value + self.stop_offset),' mm']))

    def start_bending(self):
        self.running = True
        threading.Thread(target=self.bend,args=[self.fl_set_angle]).start()
        self.button_2["state"] = "disabled"
        return

    def bend(self, set_angle):
        while self.running == True :

            while(self.fl_current_angle < set_angle and self.running==True):
                    print("Moving up")
                    time.sleep(1)
                    self.fl_current_angle =300.0

            while(self.fl_current_angle > 0 and self.running==True):
                    print("Moving down")
                    time.sleep(1)
                    self.fl_current_angle = 0.0
            self.running = False
            self.button_2["state"] = "normal"
            return
        self.button_2["state"] = "normal"
        return


    def stop_bending(self):
        self.running = False
        print("Bending is stopped")


# -------------------- Start Mainloop --------------------



if __name__ == "__main__":
    window = Tk()
    window.geometry("1440x1024")
    window.configure(bg = "#FFFFFF")
    window.resizable(True, True)
    gui = GUI(window)
    window.mainloop()


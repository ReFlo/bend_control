
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

import configparser
from pickletools import int4
import threading
import queue
import time
from pathlib import Path
from numpy import False_
from pigpio_encoder.rotary import Rotary
import pigpio



# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Menu, Toplevel, StringVar
import tkinter
from tkinter.constants import DISABLED


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

CONFIG = 'Settings.INI'

PIN_UP = 20
PIN_DOWN = 21

PIN_REMOTE_START = 23
PIN_REMOTE_STOP = 24

def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

class GUI():

    def __init__(self,parent):
        self.str_angle = str()
        self.stop_offset = float()
        self.stop_value = float()
        self.fl_set_angle = float()
        self.fl_current_angle = float()
        self.fl_current_length = float()
        self.config = configparser.ConfigParser()
        self.window = parent    
        self.run_bending = False
        self.running = True
        self.start_sett = ''

        #--------- get config data--------------
        self.config.read(CONFIG)
        # self.fl_set_angle = float(self.config['DEFAULT']['set_angle'])
        # self.fl_current_length = float(self.config['DEFAULT']['length'])
        self.offset_0 = float(self.config['DEFAULT']['offset_0'])
        self.offset_1 = float(self.config['DEFAULT']['offset_1'])
        self.offset_2 = float(self.config['DEFAULT']['offset_2'])
        self.offset_3 = float(self.config['DEFAULT']['offset_3'])
        self.max_angle = float(self.config['DEFAULT']['max_angle'])

        #--------------- create GUI items ------------------
        self.create_gui()

        #---------------initialize Encoder -----------------
        self.enc = Rotary(clk_gpio=15, dt_gpio=18, sw_gpio=14)
        self.enc.setup_rotary(rotary_callback=self.get_angle,min=-3000, max=16000, debounce=1)
       
        #--------------initialize Lenghtsystem for stop ------------
        self.len_enc = Rotary(clk_gpio=13, dt_gpio=19, sw_gpio=26)
        self.len_enc.setup_rotary(rotary_callback=self.get_length, max=300000, debounce=1)

        #--------------- initialize Relay Pings
        self.pi = pigpio.pi()
        self.pi.set_mode(PIN_UP, pigpio.OUTPUT)
        self.pi.set_mode(PIN_DOWN, pigpio.OUTPUT)
        self.pi.set_glitch_filter(PIN_REMOTE_START,300)
        self.pi.set_glitch_filter(PIN_REMOTE_STOP,100)
        #--------------- Remote Pins pigpio ---------------------
        self.pi.set_mode( PIN_REMOTE_START, pigpio.INPUT)  # GPIO  23 as input
        self.pi.set_pull_up_down(PIN_REMOTE_START, pigpio.PUD_UP)
        self.pi.callback(PIN_REMOTE_START, pigpio.FALLING_EDGE, self.start_bending)
        self.pi.set_mode(PIN_REMOTE_STOP, pigpio.INPUT)  # GPIO  23 as input
        self.pi.set_pull_up_down(PIN_REMOTE_STOP, pigpio.PUD_UP)
        self.pi.callback(PIN_REMOTE_STOP, pigpio.FALLING_EDGE, self.stop_bending)



        ########## Update displays #########
        self.change_stop_offset(int(self.config['DEFAULT']['stop_offset']))
        self.setting_angle(self.config['DEFAULT']['set_angle'])
        ######### Load last values of angle and length ###############
        # self.get_angle(float(self.config['DEFAULT']['angle']))
        # self.enc.counter = int(self.config['DEFAULT']['angle'])
        # self.len_enc.counter = int(self.config['DEFAULT']['length'])

        ## open settingswindow after starting#

    ##------------------- create grafic parts of gui -----------------   
    def create_gui(self):
        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 800,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.stop_bending(),
            relief="flat",
            state="disabled"
        )
        self.button_1.place(
            x=484.0,
            y=645.0,
            width=265.0,
            height=100.0
        )

        self.button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.start_bending(),
            relief="flat"
        )
        self.button_2.place(
            x=114.0,
            y=645.0,
            width=265.0,
            height=100.0
        )

        self.button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        self.button_3 = Button(
            bg = "#FFFFFF",
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_stop_offset(4),
            relief="flat",
            activebackground="red" 
        )
        self.button_3.place(
            x=644.0,
            y=495.0,
            width=100.0,
            height=100.0
        )


        self.button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        self.button_4 = Button(
            bg = "#FFFFFF",
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_stop_offset(3),
            relief="flat",
            activebackground="red"            

        )
        self.button_4.place(
            x=484.0,
            y=495.0,
            width=100.0,
            height=100.0
        )


        self.button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        self.button_5 = Button(
            bg = "#FFFFFF",
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_stop_offset(2),
            relief="flat",
            activebackground="red" 
        )
        self.button_5.place(
            x=284.0,
            y=495.0,
            width=100.0,
            height=100.0
        )

        self.button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        self.button_6 = Button(
            bg = "grey",
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.change_stop_offset(1),
            relief="flat",
            activebackground="red" 
        )
        self.button_6.place(
            x=114.0,
            y=495.0,
            width=100.0,
            height=100.0
        )

        self.button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        self.button_7 = Button(
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('Enter'),
            relief="flat",
            state="disabled"
        )
        self.button_7.place(
            x=791.0,
            y=645.0,
            width=380.0,
            height=100.0
        )

        self.button_image_8 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        self.button_8 = Button(
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('0'),
            relief="flat"
        )
        self.button_8.place(
            x=791.0,
            y=495.0,
            width=100.0,
            height=100.0
        )

        self.button_image_9 = PhotoImage(
            file=relative_to_assets("button_9.png"))
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('.'),
            relief="flat"
        )
        self.button_9.place(
            x=931.0,
            y=495.0,
            width=100.0,
            height=100.0
        )
        
        self.button_image_10 = PhotoImage(
            file=relative_to_assets("button_10.png"))
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.add_digit_to_angle('C'),
            relief="flat"
        )
        self.button_10.place(
            x=1071.0,
            y=495.0,
            width=100.0,
            height=100.0
        )
        self.button_10.bind("<Button-3>",self.open_settings)

        self.button_image_11 = PhotoImage(
            file=relative_to_assets("button_11.png"))
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('7'),
            relief="flat"
        )
        self.button_11.place(
            x=791.0,
            y=355.0,
            width=100.0,
            height=100.0
        )

        self.button_image_12 = PhotoImage(
            file=relative_to_assets("button_12.png"))
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('8'),
            relief="flat"
        )
        self.button_12.place(
            x=931.0,
            y=355.0,
            width=100.0,
            height=100.0
        )

        self.button_image_13 = PhotoImage(
            file=relative_to_assets("button_13.png"))
        self.button_13 = Button(
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('9'),
            relief="flat"
        )
        self.button_13.place(
            x=1071.0,
            y=355.0,
            width=100.0,
            height=100.0
        )

        self.button_image_14 = PhotoImage(
            file=relative_to_assets("button_14.png"))
        self.button_14 = Button(
            image=self.button_image_14,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('4'),
            relief="flat"
        )
        self.button_14.place(
            x=791.0,
            y=215.0,
            width=100.0,
            height=100.0
        )

        self.button_image_15 = PhotoImage(
            file=relative_to_assets("button_15.png"))
        self.button_15 = Button(
            image=self.button_image_15,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('5'),
            relief="flat"
        )
        self.button_15.place(
            x=931.0,
            y=215.0,
            width=100.0,
            height=100.0
        )

        self.button_image_16 = PhotoImage(
            file=relative_to_assets("button_16.png"))
        self.button_16 = Button(
            image=self.button_image_16,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('6'),
            relief="flat"
        )
        self.button_16.place(
            x=1071.0,
            y=215.0,
            width=100.0,
            height=100.0
        )
        
        self.button_image_17 = PhotoImage(
            file=relative_to_assets("button_17.png"))
        self.button_17 = Button(
            image=self.button_image_17,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('3'),
            relief="flat"
        )
        self.button_17.place(
            x=1071.0,
            y=75.0,
            width=100.0,
            height=100.0
        )
        
        self.button_image_18 = PhotoImage(
            file=relative_to_assets("button_18.png"))
        self.button_18 = Button(
            image=self.button_image_18,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('2'),
            relief="flat"
        )
        self.button_18.place(
            x=931.0,
            y=75.0,
            width=100.0,
            height=100.0
        )

        self.button_image_19 = PhotoImage(
            file=relative_to_assets("button_19.png"))
        self.button_19 = Button(
            image=self.button_image_19,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_digit_to_angle('1'),
            relief="flat"
        )
        self.button_19.place(
            x=791.0,
            y=75.0,
            width=100.0,
            height=100.0
        )

        self.canvas.create_rectangle(
            451.0,
            355.0,
            751.0,
            455.0,
            fill="#C4C4C4",
            outline="")

        self.current_length = self.canvas.create_text(
            601.0,
            405.0,
            anchor="center",
            text="0.0",
            fill="#000000",
            font=("Roboto", 64 * -1)
        )

        self.canvas.create_text(
            114.0,
            405.0,
            anchor="w",
            text="Anschlag:",
            fill="#000000",
            font=("Roboto", 64 * -1)
        )

        self.canvas.create_rectangle(
            451.0,
            215.0,
            751.0,
            315.0,
            fill="#C4C4C4",
            outline="")

        self.current_angle = self.canvas.create_text(
            601.0,
            265.0,
            anchor="center",
            text="0°",
            fill="#000000",
            font=("Roboto", 64 * -1)
        )

        self.canvas.create_text(
            114.0,
            265.0,
            anchor="w",
            text="Ist:",
            fill="#000000",
            font=("Roboto", 64 * -1)
        )

        self.canvas.create_rectangle(
            451.0,
            75.0,
            751.0,
            175.0,
            fill="#C4C4C4",
            outline="")

        self.set_angle = self.canvas.create_text(
            601.0,
            125.0,
            anchor="center",
            text="0°",
            fill="#000000",
            font=("Roboto", 64 * -1)
        )

        self.canvas.create_text(
            109.0,
            125.0,
            anchor="w",
            text="Soll:",
            fill="#000000",
            font=("Roboto", 64 * -1)
        )
        
    def add_digit_to_angle(self, value):

        if value == 'C':
            self.start_sett = self.start_sett + value
            if self.start_sett =='CCCCC':
                self.start_sett=''
                self.open_settings()
                return
            self.str_angle = str()
            self.canvas.itemconfig(self.set_angle, text=''.join([self.str_angle,'°']))
            self.button_7['state']='disable'
            return

        if value == 'Enter':
            self.prev_ins = ""
            if float(self.str_angle) <= self.max_angle:
                self.setting_angle(self.str_angle)
                self.str_angle = str()
                self.button_7['state']='disable'
            return

        self.str_angle = self.str_angle + value
        self.canvas.itemconfig(self.set_angle, text=''.join([self.str_angle,'°']))
        self.button_7['state']='normal'
        self.start_sett = ''

    def setting_angle(self, angle):
        try:
            result = eval(angle)
            print(result)
            self.canvas.itemconfig(self.set_angle, text=''.join([str(result),'°']))
            self.fl_set_angle = float(result)
            self.config.set('DEFAULT','set_angle',str(result))
            with open(CONFIG,'w') as file:
                self.config.write(file)

        except Exception as e:
            print(e)
            self.canvas.itemconfig(self.set_angle, text='Error')

    def change_selected_button(self, button):
        self.button_3["bg"]="white"
        self.button_4["bg"]="white"
        self.button_5["bg"]="white"
        self.button_6["bg"]="white"
        button["bg"]="red"
        return

    def change_stop_offset(self, value):
        if value == 1:
            self.stop_offset = self.offset_0
            self.change_selected_button(self.button_6)
        elif value == 2:
            self.stop_offset = self.offset_1
            self.change_selected_button(self.button_5)
        elif value == 3:
            self.stop_offset = self.offset_2
            self.change_selected_button(self.button_4)
        elif value == 4:
            self.stop_offset = self.offset_3
            self.change_selected_button(self.button_3)
        str_offset= str(self.stop_offset)
        self.config.set("DEFAULT",'stop_offset', str(value))
        with open(CONFIG,'w') as file:
            self.config.write(file)
        print(''.join(["Aktueller Anschlagoffset: ", str_offset]))
        self.display_current_length()
        return
    
    def display_current_angle(self):
        if self.fl_current_angle>=0:
            self.canvas.itemconfigure(self.current_angle, text=''.join([f'{self.fl_current_angle:.1f}',"°"]))
        else:
            self.canvas.itemconfigure(self.current_angle, text=''.join(['0.0',"°"]))
    
    def display_current_length(self):
        self.canvas.itemconfig(self.current_length, text=str(self.fl_current_length+ self.stop_offset))
  
    def start_bending(self,gpio=0, level=0, tick=0):
        print("start bending")
        if self.run_bending==False:
            self.run_bending = True
            self.button_2['state'] = 'disabled'
            self.button_1['state'] = 'normal'
            threading.Thread(target=self.bend,args=[self.fl_set_angle]).start()
        return

    def print_callback(self, a, n ,c):
        print(f"callback {c}")


    def bend(self, set_angle):
        while self.run_bending == True :

            while(self.fl_current_angle < (set_angle-0.9) and self.run_bending==True):
                    # print("Moving up")
                    self.pi.write(PIN_UP, 1)
                    time.sleep(0.00001)
                    # print(self.fl_current_angle)
            self.pi.write(PIN_UP, 0)

            time.sleep(1)

            while(self.fl_current_angle > 1.0 and self.run_bending==True):
                    # print("Moving down")
                    self.pi.write(PIN_DOWN, 1)
                    time.sleep(0.00001)
            self.pi.write(PIN_DOWN, 0)
            self.run_bending = False
            self.button_2["state"] = "normal"
            self.button_1['state'] = 'disabled'
            return
        self.button_2["state"] = "normal"
        self.button_1['state'] = 'disabled'
        return

    def stop_bending(self, gpio=0, level=0, tick=0):
        if self.run_bending == True:
            self.run_bending = False
            self.pi.write(PIN_UP, 0)
            self.pi.write(PIN_DOWN, 0)
            print("Bending is stopped")
            self.button_1['state'] = 'disabled'
            self.button_2['state'] = 'normal'

    def get_angle(self, angle):
        self.fl_current_angle = angle/10
        # self.config.set('DEFAULT','angle', str(int(angle)))
        # self.config.write(self.file)
        self.display_current_angle()

    def get_length(self, length):
        self.fl_current_length = length/20
        # self.config.set('DEFAULT','length', str(int(length)))
        # self.config.write(self.file)
        self.canvas.itemconfigure(self.current_length, text=f'{self.fl_current_length + self.stop_offset:.1f}')

    def on_closing(self):
        self.running = False
        self.run_bending = False
        self.window.destroy()

    def open_settings(self,event=None):
        try:
            if self.sett_window.state() == "normal":
                self.sett_window.focus()
        except:
            self.sett_window = Toplevel(self.window)
            self.sett_window.attributes("-fullscreen", True) 
            self.sett_class = SETTINGS(self.sett_window,self)
            self.sett_window.lift()
 
    def reset_angle(self,single):
        print("reset angle")
        self.enc.counter = 0
        self.fl_current_angle = 0.0
        if self.init_class:
            if single == 0:
                self.init_class.init_canvas.itemconfigure(self.init_class.init_text, text="Anschlag auf Nullstellung fahren und mit Enter bestätigen")
                self.init_class.init_button_1["command"] = self.reset_length 
            else:
                del self.init_class
                self.init_window.destroy()


    def reset_length(self):
        print("reset length")
        self.len_enc.counter = 0
        self.fl_current_length = 0
        self.display_current_length()
        if self.init_class:
            del self.init_class
            self.init_window.destroy()

    def initialize(self,mode,single=0):
        self.init_window = Toplevel(self.window)
        self.init_window.attributes("-fullscreen", True) 
        self.init_class = INIT(self.init_window,self,mode,single)

    def close_settings(self):
        if self.sett_class:
            del self.sett_class
            self.sett_window.destroy()
        
class SETTINGS():
    def __init__(self,sett_window,gui) -> None:
        super().__init__()
        #-------------------- create Settingspage ---------------------------

        self.sett_window = sett_window

        self.canvas = Canvas(
            self.sett_window,
            bg = "#FFFFFF",
            height = 800,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
        
        self.reset_image_1 = PhotoImage(
            file=relative_to_assets("reset_2.png"))

        self.reset_button_1 = Button(
            self.sett_window,
            image=self.reset_image_1,
            text="test",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui.initialize("angle",1),
            relief="flat"
        )
        self.reset_button_1.place(
            x=720.0,
            y=75.0,
            width=380.0,
            height=100.0
        )

        self.reset_image_2 = PhotoImage(
            file=relative_to_assets("reset_2.png"))
        
        self.reset_button_2 = Button(
            self.sett_window,
            image=self.reset_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui.initialize("length",1),
            relief="flat"
        )
        self.reset_button_2.place(
            x=720.0,
            y=200.0,
            width=380.0,
            height=100.0
        )

        self.button_finished_image = PhotoImage(
            file=relative_to_assets("button_finish.png"))
        
        self.button_finished = Button(
            self.sett_window,
            image=self.button_finished_image,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: gui.close_settings(),
            relief="flat"
        )
        self.button_finished.place(
            x=720.0,
            y=500.0,
            width=380.0,
            height=100.0
        )



        self.canvas.create_text(
            200.0,
            125.0,
            anchor="w",
            text="Winkel:",
            fill="#000000",
            font=("Roboto", 64 * -1)
        )

        self.canvas.create_text(
            200.0,
            250.0,
            anchor="w",
            text="Anschlag:",
            fill="#000000",
            font=("Roboto", 64 * -1)
        )
       
class INIT():
    def __init__(self,init_window,gui,mode,single) -> None:

        self.init_canvas = Canvas(
            init_window,
            bg = "#FFFFFF",
            height = 800,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.init_canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)

        self.init_button_1 = Button(
                init_window,
                image=gui.button_image_7,
                text="Enter",
                borderwidth=0,
                highlightthickness=0,
                relief="flat"
            )

        if mode == "angle":
            self.init_button_1['command']=lambda: gui.reset_angle(single)
            text = "Biegewange auf Nullstellung fahren und mit Enter bestätigen"
        elif mode == "length":
            self.init_button_1['command']=lambda: gui.reset_length()
            text = "Anschlag auf Nullstellung fahren und mit Enter bestätigen"

        self.init_button_1.place(
            x=460.0,
            y=500.0,
            width=380.0,
            height=100.0
        )

        self.init_text=self.init_canvas.create_text(
            640.0,
            200.0,
            anchor="c",
            text=text,
            fill="#000000",
            font=("Roboto", 64 * -1),
            width = 1200,
            justify='center' 
        )



# -------------------- Start Mainloop --------------------
if __name__ == "__main__":
    window = Tk()
    # window.attributes("-fullscreen", True) 
    window.geometry("1280x800")
    window.configure(bg = "#FFFFFF")
    window.resizable(True, True)
    gui = GUI(window)
    window.protocol("WM_DELETE_WINDOW", gui.on_closing)
    window.after(10,lambda: gui.initialize("angle",0))
    window.mainloop()


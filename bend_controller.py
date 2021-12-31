#bend_controller

import tkinter as tk
from tkinter import ttk


window = tk.Tk()
window.geometry('800x600')
window.title('Bend Controller')
styles=ttk.Style().theme_names()
ttk.Style().theme_use('vista')


gui_items = list()
angle = str()
fl_angle = float()

button_values = ['1','2','3','4','5','6','7','8','9','0','.','C']

############### Arch adding ######################

def add_digit_to_arch(value):
    global angle

    if value == 'C':
        angle = str()
        output_label['text'] = '...'
        return

    if value == 'ENTER':
        change_angle(angle)
        angle = str()
        return

    angle = angle + value
    output_label['text'] = angle


def change_angle(angle):
    global fl_angle
    try:
        result = eval(angle)
        print(result)
        output_label['text'] = result
        fl_angle = float(result)


    except Exception as e:
        print(e)
        output_label['text'] = 'Error'



############## Window preperations ##############
def create_button(value):
    button=tk.Button(text=value, command=lambda: add_digit_to_arch(value))
    gui_items.append(button)

for val in button_values:
    create_button(val)

################ Creating Grid for GUI ##############
output_label = tk.Label(text='Bitte Winkel eingeben')
output_label.grid(row=0, columnspan=10)


# All buttons will be auto-placed in a grid
# with maximum 3 columns and endless rows here:
column_count = 0
row_count = 1
maximum_columns = 3

for item in gui_items:
    item.grid(row=row_count, column=column_count)

    column_count += 1
    if column_count == maximum_columns:
        column_count = 0
        row_count += 1

create_button('ENTER')
gui_items[12].grid(row=row_count+1, column=0, columnspan=3)

if __name__ == '__main__':
    window.mainloop()
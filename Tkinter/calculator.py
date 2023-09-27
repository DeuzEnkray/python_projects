import os
from tkinter import *

display_text = str()


def button_maker(txt):
    temp_button = Button(window,
                         text=txt,
                         font=('Segoe UI', 15),
                         fg='black',
                         background='#72bcd4',
                         activebackground='#3a9fbf',
                         relief=RAISED,
                         bd=3,
                         padx=5, pady=5,
                         width=64, height=64,
                         compound='center',
                         image=placeHolder,
                         command=lambda: click(txt))
    return temp_button


def number_format(operation):
    global display_text
    display_text = display_text.replace(' ', '')
    return display_text.split(operation)


def display_format():
    global display_text
    temp_text = str()
    for i in display_text:
        temp_text += i + ' '
    display_text = temp_text


def click(inp):
    global display_text
    if inp == 'CLR':
        display_text = str()
    elif inp == '=':
        if '+' in display_text:
            calc_add()
        elif '-' in display_text:
            calc_sub()
        elif '*' in display_text:
            calc_mul()
        elif '/' in display_text:
            calc_div()
    else:
        display_text = display_text + ' ' + inp
    calculator_screen.config(text=display_text)


def calc_add():
    global display_text
    inp_num = number_format('+')
    display_text = str(round(float(inp_num[0]) + float(inp_num[1]), 2))
    display_format()
    calculator_screen.config(text=display_text)


def calc_sub():
    global display_text
    inp_num = number_format('-')
    display_text = str(round(float(inp_num[0]) - float(inp_num[1]), 2))
    display_format()
    calculator_screen.config(text=display_text)


def calc_mul():
    global display_text
    inp_num = number_format('*')
    display_text = str(round(float(inp_num[0]) * float(inp_num[1]), 2))
    display_format()
    calculator_screen.config(text=display_text)


def calc_div():
    global display_text
    inp_num = number_format('/')
    display_text = str(round(float(inp_num[0]) / float(inp_num[1]), 2))
    display_format()
    calculator_screen.config(text=display_text)

window = Tk()

window.geometry("370x580")
window.title("Calculator")
window.iconphoto(True, icon)
window.config(background="#ADD8E6")

calculator_screen = Label(window,
                          background='white',
                          foreground='black',
                          font=('Segoe UI', 15),
                          relief=SUNKEN,
                          bd=3,
                          image=placeHolder,
                          compound='center',
                          width=346, height=194)

button_one = button_maker('1')
button_two = button_maker('2')
button_three = button_maker('3')
button_four = button_maker('4')
button_five = button_maker('5')
button_six = button_maker('6')
button_seven = button_maker('7')
button_eight = button_maker('8')
button_nine = button_maker('9')
button_zero = button_maker('0')
button_clr = button_maker('CLR')
button_add = button_maker('+')
button_sub = button_maker('-')
button_mul = button_maker('*')
button_div = button_maker('/')
button_equal = button_maker('=')

calculator_screen.place(x=10, y=10)
button_one.place(x=10, y=220)
button_two.place(x=100, y=220)
button_three.place(x=190, y=220)
button_four.place(x=10, y=310)
button_five.place(x=100, y=310)
button_six.place(x=190, y=310)
button_seven.place(x=10, y=400)
button_eight.place(x=100, y=400)
button_nine.place(x=190, y=400)
button_zero.place(x=100, y=490)
button_clr.place(x=280, y=220)
button_add.place(x=280, y=310)
button_sub.place(x=280, y=400)
button_div.place(x=10, y=490)
button_mul.place(x=190, y=490)
button_equal.place(x=280, y=490)

window.resizable(False, False)
window.mainloop()

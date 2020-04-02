# Project: Simple Python GUI
# Author: Sonny STACKPYTHON
# Date Created: April 2, 2020

from tkinter import *

gui = Tk()
gui.geometry("550x550")
gui.title("STACKPYTHON")

# Define navigation message
name_message = str("Nice to meet you mr.")
age_message = str("Your age is :")


def enter_name():
    name_label = Label(gui)
    name_label.pack()
    output_name_txt = name_message + str(inp_name.get())
    name_label.config(text=output_name_txt,
                      font=("Courier", 12),
                      bd=10,
                      width=200)


# Navigation message (name)
name_guide_label = Label(text='Type your name here',
                         font=("Courier", 12)).pack()

# Form built for retrieving input data (name)
inp_name = StringVar()
name_val = Entry(gui, textvariable=inp_name).pack()


name_btn = Button(text="Enter",
                  height=4,
                  width=8,
                  fg='white',
                  command=enter_name,
                  bg='navy',
                  bd=5,
                  variable=name_val).pack()


# Navigation message (age)
age_guide_label = Label(text='Type your age here',
                        font=("Courier", 12)).pack()

# Form built for retrieving input data (age)
inp_age = IntVar()
age_val = Spinbox(gui,
                  from_=18,
                  to=30,
                  textvariable=inp_age)


age_val.pack(side=TOP,)


def enter_age():
    age_label = Label(gui)
    age_label.pack()
    output_age_txt = age_message + str(inp_age.get())
    age_label.config(text=output_age_txt,
                     font=("Courier", 12),
                     bd=10,
                     width=200)


age_btn = Button(gui, text="Enter",
                 height=4,
                 width=8,
                 command=enter_age,
                 bd=5,
                 bg='navy',
                 fg='white').pack()


def quite():
    quit_btn = Button(text='Quit',
                      command=gui.quit,
                      height=4,
                      width=8,
                      bg='gold',
                      bd=5)
    quit_btn.pack(side=TOP,
                  padx=1,
                  pady=1)


quite()
gui.mainloop()










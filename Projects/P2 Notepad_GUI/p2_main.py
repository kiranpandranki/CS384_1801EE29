from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import re
import time


def new_file():
    pass


def open_file():
    pass


def save_file():
    pass


def save_as():
    pass


def delete():
    pass


def find_func(find_input):
    pass


def find():
    pass


def find_and_replace():
    pass


def word_count():
    pass


def char_count():
    pass


def created_time():
    pass


def modified_time():
    pass


root = Tk()
root.geometry('733x434')
root.title("Untitled-Notepad")
root.wm_iconbitmap("notepad.ico")
file = None
# For Entering Text...
text_space = Text(root, font="Times 18", bg="blue")
text_space.pack(expand=True, fill=BOTH)
####################################
Main_menu = Menu(root)

# File Menu...
File_menu = Menu(Main_menu, tearoff=0)
File_menu.add_command(label='New', command=new_file,
                      font='times')
File_menu.add_command(label='Open', command=open_file,
                      font='times')
File_menu.add_command(label='Save', command=save_file, font='times')
File_menu.add_command(label='Save as', command=save_as, font='times')
File_menu.add_separator()
File_menu.add_command(label='Delete', command=delete, font='times')
File_menu.add_command(label='Exit', command=quit, font='times')
Main_menu.add_cascade(label='File', font='times', menu=File_menu)
#####################################
# Edit Menu...
Edit_menu = Menu(Main_menu, tearoff=0)
Edit_menu.add_command(label='Cut',
                      command=lambda: text_space.event_generate("<<Cut>>"), font='times', accelerator="Ctrl+X")
Edit_menu.add_command(label='Copy',
                      command=lambda: text_space.event_generate("<<Copy>>"), font='times', accelerator="Ctrl+P")
Edit_menu.add_command(label='Paste',
                      command=lambda: text_space.event_generate("<<Paste>>"), font='times', accelerator="Ctrl+V")
Edit_menu.add_separator()
Edit_menu.add_command(label='Find', command=find,
                      font='times')
Edit_menu.add_command(label='Find and Replace',
                      command=find_and_replace, font='times')
Edit_menu.add_command(
    label='Clear all', command=lambda: text_space.delete(1.0, END), font='times')
Main_menu.add_cascade(menu=Edit_menu, label='Edit', font='times')
#####################################
# Stats Menu...
Stats_menu = Menu(Main_menu, tearoff=0)
Stats_menu.add_command(label='Word Count', command=word_count, font='times')
Stats_menu.add_command(label='Char Count', command=char_count, font='times')
Stats_menu.add_separator()
Stats_menu.add_command(label='Created Time',
                       command=created_time, font='times')
Stats_menu.add_command(label='Modified Time',
                       command=modified_time, font='times')
Main_menu.add_cascade(menu=Stats_menu, label='Stats', font='times')
#####################################

root.config(menu=Main_menu)
scroll_bar = Scrollbar(text_space)
scroll_bar.pack(side=RIGHT, fill=Y)
scroll_bar.config(command=text_space.yview)
text_space.config(yscrollcommand=scroll_bar.set)
root.mainloop()

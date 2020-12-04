from tkinter import *
from tkinter.messagebox import showinfo
import sqlite3
import csv
import os
import datetime
import hashlib
import pandas as pd
import time as t
cwd = os.getcwd()

def main_menu():
  main_menu_frame = Frame(root, bg='grey')
  Button(main_menu_frame, text='Register', width=20, relief=RIDGE,
         command=lambda: [register(), main_menu_frame.destroy()]).pack()
  Button(main_menu_frame, text='Login', width=20, relief=RIDGE,
         command=lambda: [login(), main_menu_frame.destroy()]).pack()
  Button(main_menu_frame, text='Exit', width=20,
         relief=RIDGE, command=quit).pack()
  main_menu_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
def register():
  pass
def login():
  pass

root = Tk()
root.geometry("1100x300")
main_menu()
root.mainloop()

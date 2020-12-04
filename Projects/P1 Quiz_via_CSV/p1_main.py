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
    def back():
        register_frame.destroy()
        main_menu()

    def submit():
        for i in range(5):
            if not text_variable_list[i].get():
                showinfo('Error', 'Fill all credentials!')
                return
        with sqlite3.connect('project1_quiz_cs384.db') as db:
            cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS project1_registration(
        userID INTEGER PRIMARY KEY,
        username VARCHAR(20) NOT NULL,
        password VARCHAR(20) NOT NULL,
        name VARCHAR(20) NOT NULL,
        whatsapp_number VARCHAR(20) NOT NULL)
        ''')
        find_user = 'SELECT * FROM project1_registration WHERE username = ?'
        cursor.execute(find_user, [(text_variable_list[1].get())])
        if cursor.fetchall():
            showinfo('Error', 'Username already exists!')
        else:
            if text_variable_list[2].get() != text_variable_list[3].get():
                showinfo('Error', 'Password does not match!')

                entry_list[2].delete(0, END)
                entry_list[3].delete(0, END)

                entry_list[2].update()
                entry_list[3].update()
                return
            if not text_variable_list[4].get().isdigit():
                showinfo('Error', 'Enter a valid Whatsapp number!')
                entry_list[4].delete(0, END)
                entry_list[4].update()
                return

            hash_password_temp = hashlib.sha224(
                text_variable_list[2].get().encode()).hexdigest()
            data_list = [(text_variable_list[1].get()), (hash_password_temp), (text_variable_list[0].get().capitalize()),
                         (text_variable_list[4].get())]
            cursor.execute("""
            INSERT INTO project1_registration(username,password,name,whatsapp_number)
            VALUES(?,?,?,?)
            """, data_list)
            db.commit()
            showinfo('', 'Registration Successful!')
        back()

    register_list = ['Name', 'Roll', 'Password',
                     'Confirm Password', 'Whatsapp Number']
    label_list = []
    entry_list = []
    text_variable_list = []
    register_frame = Frame(root)
    for i in range(5):
        label_list.append(Label(register_frame, text=register_list[i] + '  :'))
        label_list[i].grid(row=i + 1, column=0, sticky=W, padx=5)
        text_variable_list.append(StringVar())
        if i == 3 or i == 2:
            entry_list.append(
                Entry(register_frame, textvariable=text_variable_list[i], show='*'))
        else:
            entry_list.append(
                Entry(register_frame, textvariable=text_variable_list[i]))
        entry_list[i].grid(row=i + 1, column=1, padx=5)

    register_button = Button(
        register_frame, text='Register', command=submit, relief=GROOVE)
    back_button = Button(register_frame, text='Back',
                         command=back, relief=GROOVE)
    register_button.grid(row=6, column=0, pady=10)
    back_button.grid(row=6, column=1, pady=10)
    register_frame.place(relx=0.5, rely=0.5, anchor=CENTER)


def login():
  pass

root = Tk()
root.geometry("1100x300")
main_menu()
root.mainloop()

from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import re
import time


def new_file():
    global file
    ans = msg.askyesnocancel("Notepad", 'Do you want to save this file?')
    if ans:
        save_file()
        root.title('Untitled-Notepad')
        file = None
        text_space.delete(1.0, END)
    elif not ans:
        root.title('Untitled-Notepad')
        file = None
        text_space.delete(1.0, END)


def open_file():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", '*.*'), ("Text Documents", "*.txt"), ("Python Files", '*.py')])
    if file == "":
        file = None
    else:
        try:
            f = open(file, 'r')
            root.title(os.path.basename(file + " - Notepad"))
            text_space.delete(1.0, END)
            text_space.insert(1.0, f.read())
            f.close()
        except:
            msg.showinfo("File open error:",
                         "This kind of file cannot be opened !")


def save_file():
    global file
    if file is None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension='.txt',
                                 filetype=[("All Files", "*.*"), ("Text Documents", '*.txt')])
        if file == "":
            file = None
        else:
            f = open(file, 'w')
            f.write(text_space.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + ' - Notepad')
    else:
        f = open(file, 'w')
        f.write(text_space.get(1.0, END))
        f.close()


def save_as():
    global file
    if file is None:
        save_file()
    else:
        file = asksaveasfilename(initialfile=os.path.basename(file), defaultextension='.txt',
                                 filetype=[("All Files", "*.*"), ("Text Documents", '*.txt')])
        if file == '':
            file = None
        else:
            f = open(file, 'w')
            f.write(text_space.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + ' - Notepad')


def delete():
    global file
    if file is None:
        msg.showinfo("Delete Error!", "The current file is not yet saved")
    else:
        ans = msg.askyesno("Confirmation question:", "Do you really want to delete " + os.path.basename(file))
        if ans:
            text_space.delete(1.0, END)
            root.title('Untitled - Notepad')
            os.unlink(file)
            msg.showinfo("Deleted Successfully!", "Successfully deleted " + os.path.basename(file))
            file = None


def find_func(find_input):
    word = find_input.get()
    text_space.tag_remove("match", "1.0", END)
    matches = 0
    if word:
        start_pos = '1.0'
        while True:
            start_pos = text_space.search(word, start_pos, END)
            if not start_pos:
                break
            end_pos = f'{start_pos} + {len(word)}c'
            text_space.tag_add('match', start_pos, end_pos)
            matches += 1
            start_pos = end_pos
            text_space.tag_config("mathc", foreground='red', background='yellow')


def find():
    def find_close():
        text_space.tag_remove('match', '1.0', END)
        find_popup.destroy()

    find_popup = Toplevel()
    find_popup.geometry("400x200")
    find_popup.wm_iconbitmap('notepad.ico')
    find_popup.title("Find")
    find_popup.resizable(0, 0)
    # Creating Labelframe
    find_frame = LabelFrame(find_popup, text="Find")
    find_frame.pack(pady=30)
    # Creating label for find
    find_word = Label(find_frame, text="Find")
    # Creating entry for find
    find_input = Entry(find_frame, width=30)
    # Creating button for find
    find_button = Button(find_frame, text="Find", command=lambda: find_func(find_input))
    close_button = Button(find_frame, text="Close", command=find_close)
    # Creating grids for find and replace
    find_word.grid(row=0, column=0, padx=5, pady=5)
    find_input.grid(row=0, column=1, padx=5, pady=5)
    find_button.grid(row=2, column=0, padx=30, pady=5)
    close_button.grid(row=2, column=1, padx=30, pady=5)


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
text_space = Text(root, font="Times 18")
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

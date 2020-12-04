
# 1801EE29 - Pandranki Kiran
# 1801EE24 - Rishi Kanth


from tkinter import *
import tkinter.messagebox as msg
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import re
import time


def new_file(event=''):
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


def open_file(event=''):
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


def save_file(event=''):
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


def save_as(event=''):
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


def delete(event=''):
    global file
    if file is None:
        msg.showinfo("Delete Error!", "The current file is not yet saved")
    else:
        ans = msg.askyesno("Confirmation question:",
                           "Do you really want to delete " + os.path.basename(file))
        if ans:
            text_space.delete(1.0, END)
            root.title('Untitled - Notepad')
            os.unlink(file)
            msg.showinfo("Deleted Successfully!",
                         "Successfully deleted " + os.path.basename(file))
            file = None


def find_func(find_input):
    word = find_input.get()
    text_space.tag_remove("match", "1.0", END)
    matches = 0
    if word:
        start_pos = '1.0'
        while True:
            start_pos = text_space.search(word, start_pos, stopindex=END)
            if not start_pos:
                break
            end_pos = f'{start_pos} + {len(word)}c'
            text_space.tag_add('match', start_pos, end_pos)
            matches += 1
            start_pos = end_pos
            text_space.tag_config(
                "match", foreground='red', background='yellow')


def find(event=''):
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
    find_button = Button(find_frame, text="Find",
                         command=lambda: find_func(find_input))
    close_button = Button(find_frame, text="Close", command=find_close)
    # Creating grids for find and replace
    find_word.grid(row=0, column=0, padx=5, pady=5)
    find_input.grid(row=0, column=1, padx=5, pady=5)
    find_button.grid(row=2, column=0, padx=30, pady=5)
    close_button.grid(row=2, column=1, padx=30, pady=5)


def find_and_replace(event=''):
    def replace():
        find_word = find_input.get()
        replace_word = replace_input.get()
        text = text_space.get(1.0, END)
        new_text = text.replace(find_word, replace_word)
        text_space.delete(1.0, END)
        text_space.insert(1.0, new_text)

    def find_replace_close():
        text_space.tag_remove("match", "1.0", END)
        find_replace_popup.destroy()

    find_replace_popup = Toplevel()
    find_replace_popup.geometry("400x300")
    find_replace_popup.wm_iconbitmap('notepad.ico')
    find_replace_popup.title("Find and Replace")
    find_replace_popup.resizable(0, 0)
    # Creating Labelframe
    find_frame = LabelFrame(find_replace_popup, text="Find and Replace")
    find_frame.pack(pady=30)
    # Creating labels for find and replace
    find_word = Label(find_frame, text="Find")
    replace_word = Label(find_frame, text="Replace")
    # Creating entries for find and replace
    find_input = Entry(find_frame, width=30)
    replace_input = Entry(find_frame, width=30)
    # Creating buttons for find and replace
    find_button = Button(find_frame, text="Find",
                         command=lambda: find_func(find_input))
    replace_button = Button(find_frame, text="Replace", command=replace)
    close_button = Button(find_frame, text="Close",
                          command=lambda: find_replace_close())
    # Creating grids for find and replace
    find_word.grid(row=0, column=0, padx=5, pady=5)
    replace_word.grid(row=1, column=0, padx=5, pady=5)
    find_input.grid(row=0, column=1, padx=5, pady=5)
    replace_input.grid(row=1, column=1, padx=5, pady=5)
    find_button.grid(row=2, column=0, padx=10, pady=5)
    replace_button.grid(row=2, column=1, padx=10, pady=5)
    close_button.grid(row=2, column=2, padx=10, pady=5)


def word_count(event=''):
    text_var = text_space.get(1.0, END)
    word_list = text_var.split(' ')
    temp_word_list = []
    count = 0
    for x in word_list:
        temp_word_list.extend(x.split('\n'))
    for x in temp_word_list:
        if x != "":
            count += 1
    msg.showinfo("WordCount :", f"There are a {count} words in total.")


def char_count(event=''):
    text_var = text_space.get(1.0, END)
    word_list = text_var.split('\n')
    temp_word_list = []
    count = 0
    for x in word_list:
        if x != "":
            count += len(x)
    msg.showinfo("Character Count :",
                 f"There are a {count} characters in total")


def created_time(event=''):
    global file
    if file == None:
        msg.showinfo("Time Error", "No file was opened !")
    else:
        x = os.path.getctime(file)
        msg.showinfo("Created Time:",
                     f"The file {os.path.basename(file)} is Created on:\n{time.ctime(x)}")


def modified_time(event=''):
    global file
    if file == None:
        msg.showinfo("Time Error", "No file was opened !")
    else:
        x = os.path.getmtime(file)
        msg.showinfo("Last Modified Time:",
                     f"The file {os.path.basename(file)} is last modified on:\n{time.ctime(x)}")


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
root.bind('<Control-n>', new_file)
root.bind('<Control-N>', new_file)
File_menu.add_command(label='New', command=new_file,
                      font='times', accelerator='Ctrl+N')
root.bind('<Control-o>', open_file)
root.bind('<Control-O>', open_file)
File_menu.add_command(label='Open', command=open_file,
                      font='times', accelerator='Ctrl+O')
root.bind('<Control-s>', save_file)
root.bind('<Control-S>', save_file)
File_menu.add_command(label='Save', command=save_file,
                      font='times', accelerator='Ctrl+S')
File_menu.add_command(label='Save as', command=save_as, font='times')
File_menu.add_separator()
root.bind('<Control-d>', delete)
root.bind('<Control-D>', delete)
File_menu.add_command(label='Delete', command=delete,
                      font='times', accelerator='Ctrl+D')
root.bind('<Control-e>', quit)
root.bind('<Control-E>', quit)
File_menu.add_command(label='Exit', command=quit,
                      font='times', accelerator='Ctrl+E')
Main_menu.add_cascade(label='File', font='times', menu=File_menu)
#####################################
# Edit Menu...
Edit_menu = Menu(Main_menu, tearoff=0)
Edit_menu.add_command(label='Cut',
                      command=lambda: text_space.event_generate("<<Cut>>"), font='times', accelerator="Ctrl+X")
Edit_menu.add_command(label='Copy',
                      command=lambda: text_space.event_generate("<<Copy>>"), font='times', accelerator="Ctrl+C")
Edit_menu.add_command(label='Paste',
                      command=lambda: text_space.event_generate("<<Paste>>"), font='times', accelerator="Ctrl+V")
Edit_menu.add_separator()
root.bind('<Control-f>', find)
root.bind('<Control-F>', find)
Edit_menu.add_command(label='Find', command=find,
                      font='times', accelerator='Ctrl+F')
root.bind('<Control-h>', find_and_replace)
root.bind('<Control-H>', find_and_replace)
Edit_menu.add_command(label='Find and Replace',
                      command=find_and_replace, font='times', accelerator='Ctrl+H')
Edit_menu.add_command(
    label='Clear all', command=lambda: text_space.delete(1.0, END), font='times')
Main_menu.add_cascade(menu=Edit_menu, label='Edit', font='times')
#####################################
# Stats Menu...
Stats_menu = Menu(Main_menu, tearoff=0)
root.bind('<Control-w>', word_count)
root.bind('<Control-W>', word_count)
Stats_menu.add_command(label='Word Count', command=word_count,
                       font='times', accelerator='Ctrl+W')
root.bind('<Control-c><h>', char_count)
root.bind('<Control-C><H>', char_count)
Stats_menu.add_command(label='Char Count', command=char_count,
                       font='times', accelerator='Ctrl+C+H')
Stats_menu.add_separator()
root.bind('<Control-c><t>', created_time)
root.bind('<Control-C><T>', created_time)
Stats_menu.add_command(label='Created Time',
                       command=created_time, font='times', accelerator='Ctrl+C+T')
root.bind('<Control-m><t>', modified_time)
root.bind('<Control-M><T>', modified_time)
Stats_menu.add_command(label='Modified Time',
                       command=modified_time, font='times', accelerator='Ctrl+M+T')
Main_menu.add_cascade(menu=Stats_menu, label='Stats', font='times')
#####################################

root.config(menu=Main_menu)
scroll_bar = Scrollbar(text_space)
scroll_bar.pack(side=RIGHT, fill=Y)
scroll_bar.config(command=text_space.yview)
text_space.config(yscrollcommand=scroll_bar.set)
root.mainloop()

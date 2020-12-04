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
    def back():
        login_frame.destroy()
        main_menu()

    def submit():
        for i in range(2):
            if not text_variable_list[i].get():
                showinfo('Error', 'Fill all credentials!')
                return
        with sqlite3.connect('project1_quiz_cs384.db') as db:
            cursor = db.cursor()
        find_user = 'SELECT * FROM project1_registration WHERE username = ?'
        try:
            cursor.execute(find_user, [(text_variable_list[0].get())])
        except sqlite3.OperationalError:
            showinfo('Error', 'No registrations found!\nPlease register first.')
            back()
            return

        temp_list = cursor.fetchall()
        if temp_list:
            hash_password_temp = hashlib.sha224(
                text_variable_list[1].get().encode()).hexdigest()
            if hash_password_temp == temp_list[0][2]:
                login_frame.destroy()
                quiz_menu(text_variable_list[0].get())
            else:
                showinfo('Error', 'Wrong Password!')
        else:
            showinfo('Error', 'Username Not Found!')

    login_list = ['Username', 'Password']
    label_list = []
    entry_list = []
    text_variable_list = []
    login_frame = Frame(root)
    for i in range(2):
        label_list.append(Label(login_frame, text=login_list[i] + '  :'))
        label_list[i].grid(row=i + 1, column=0, sticky=W, padx=5)
        text_variable_list.append(StringVar())
        if i == 1:
            entry_list.append(
                Entry(login_frame, textvariable=text_variable_list[i], show='*'))
        else:
            entry_list.append(
                Entry(login_frame, textvariable=text_variable_list[i]))
        entry_list[i].grid(row=i + 1, column=1, padx=5)

    login_button = Button(login_frame, text='Login',
                          command=submit, relief=GROOVE)
    back_button = Button(login_frame, text='Back', command=back, relief=GROOVE)
    login_button.grid(row=6, column=0, pady=10)
    back_button.grid(row=6, column=1, pady=10)
    login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

def run_quiz(quiz_number, user_name):
    def submit():
        marks_obtained = 0
        total_marks = 0
        legend_correct_choices = 0
        legend_wrong_choices = 0
        legend_unattempted = 0
        for j in range(len(data_list)):
            total_marks += int(data_list[j][1])
            if data_list[j][3] == 'y':  # if compulsory question
                if response_list[j].get() != data_list[j][0]:
                    marks_obtained += int(data_list[j][2])
                    if response_list[j].get() != 'S':
                        legend_wrong_choices += 1
                    else:
                        legend_unattempted += 1
                else:
                    marks_obtained += int(data_list[j][1])
                    legend_correct_choices += 1
            elif data_list[j][3] == 'n':  # if not compulsory
                if response_list[j].get() == data_list[j][0]:
                    marks_obtained += int(data_list[j][1])
                    legend_correct_choices += 1
                elif response_list[j].get() != 'S':
                    marks_obtained += int(data_list[j][2])
                    legend_wrong_choices += 1
                else:
                    legend_unattempted += 1

        # to database table
        with sqlite3.connect('project1_quiz_cs384.db') as db:
            cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS project1_marks(
        serialID INTEGER PRIMARY KEY,
        roll VARCHAR(20) NOT NULL,
        quiz_num VARCHAR(20) NOT NULL,
        total_marks VARCHAR(20) NOT NULL)
        ''')
        find_user = 'SELECT * FROM project1_marks WHERE roll = ? AND quiz_num = ?'
        cursor.execute(find_user, [(user_name), (quiz_number)])
        if cursor.fetchall():
            cursor.execute(f"""
                    UPDATE project1_marks SET total_marks = ? WHERE roll = {user_name} AND quiz_num = {quiz_number}
                    """, [marks_obtained])
        else:
            cursor.execute("""
                        INSERT INTO project1_marks(roll,quiz_num,total_marks)
                        VALUES(?,?,?)
                        """, [(user_name), (quiz_number), (marks_obtained)])
        db.commit()
        scores_file_path = os.path.join(
            cwd, 'quiz_wise_responses', 'scores_q' + str(quiz_number) + '.csv')
        # to scores_qx.csv
        with open(scores_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            header_row = ['roll', 'quiz_num', 'marks_obatained']
            writer.writerow(header_row)
            cursor.execute(
                f"SELECT * FROM project1_marks WHERE quiz_num = {quiz_number} ORDER BY roll ASC")
            for db_row in cursor.fetchall():
                writer.writerow(db_row[1:4])
        # to individual responses
        individual_reponses_path = os.path.join(cwd, 'individual_responses',
                                                'q' + str(quiz_number) + '_' + user_name + '.csv')
        marked_choice_list = [x.get() for x in response_list]
        legend_total_list = [legend_correct_choices, legend_wrong_choices, legend_unattempted, marks_obtained,
                             total_marks]
        legend_list = ['Correct Choices', 'Wrong Choices',
                       'Unattempted', 'Marks Obtained', 'Total Quiz Marks']
        q_roll_df = pd.read_csv(quiz_file_path)
        q_roll_df = q_roll_df.iloc[:, :-1]

        temp_df = pd.DataFrame({'marked_choice': marked_choice_list})
        temp_df1 = pd.DataFrame(
            {'Total': legend_total_list, 'Legend': legend_list})

        temp_df = pd.concat([temp_df, temp_df1], axis=1)
        q_roll_df = pd.concat([q_roll_df, temp_df], axis=1)
        # q_roll_df['marked_choice'] = pd.DataFrame(marked_choice_list)
        # q_roll_df['Total'] = pd.DataFrame(legend_total_list)
        # q_roll_df['Legend'] = pd.DataFrame(legend_list)
        q_roll_df.to_csv(individual_reponses_path, index=False)
        quiz_menu(user_name)

    run_quiz_frame = Frame(root, bg='grey')
    instructions_frame = Frame(run_quiz_frame)
    instructions_frame.pack(fill=BOTH)
    canvas = Canvas(run_quiz_frame)
    scroll_bar = Scrollbar(
        run_quiz_frame, orient='vertical', command=canvas.yview)
    scrollable_frame = Frame(canvas)
    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(
        scrollregion=canvas.bbox('all')))
    scrollable_frame.pack(fill=BOTH)
    canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
    canvas.configure(yscrollcommand=scroll_bar.set)

    quiz_file_path = os.path.join(
        cwd, 'quiz_wise_questions', 'q' + str(quiz_number) + '.csv')

    def clock(start_time):
        present_time = t.strftime("%M:%S")
        timer = datetime.datetime.strptime(
            present_time, "%M:%S")-datetime.datetime.strptime(start_time, "%M:%S")
        second_elapsed = int(timer.total_seconds())
        second_elapsed = int(minutes)*60 - second_elapsed
        minute, second = divmod(second_elapsed, 60)
        modified_timer = "{:02d}:{:02d}".format(minute, second)
        timer_label.config(
            text='time : ' + modified_timer, font='comicsans 18 bold')
        if second_elapsed > 0:
            timer_label.after(1000, clock, start_time)
        else:
            run_quiz_frame.destroy()
            submit()

    with open(quiz_file_path, 'r') as file_read:
        reader = csv.reader(file_read)
        header_row = next(reader)

        time_ = header_row[-1][-3:-1]
        minutes = time_
        seconds = '00'
        timer_label = Label(instructions_frame, text='time : ' +
                            minutes + ':' + seconds, font='comicsans 18 bold')
        timer_label.grid(row=0, column=2, sticky='e')
        start_time = t.strftime("%M:%S")
        clock(start_time)
        response_list = []
        data_list = []
        grid_counter = 0
        question_counter = 0

        with sqlite3.connect('project1_quiz_cs384.db') as db:
            cursor = db.cursor()
        find_user = 'SELECT * FROM project1_registration WHERE username = ?'
        cursor.execute(find_user, [user_name])
        name_of_student = cursor.fetchall()[0][3]
        Label(instructions_frame,text=f"Name : {name_of_student}\nRoll : {user_name}",font='comicsans 18 bold').grid(row=grid_counter, column=0, sticky='w')
        Label(instructions_frame, text=f'''Quiz Number : {quiz_number}
                                            Test Instructions:
                                    mc -> marks awarded for correct choice
                                    mw -> marks awarded for wrong choice
                                    cp -> compulsory question or not('y':yes,'n':no)''',
              font='comicsans 18 bold'
              ).grid(row=grid_counter, column=1, sticky='w')
        grid_counter += 1
        for row in reader:
            response_list.append(StringVar(value='S'))
            data_list.append((row[6], row[7], row[8], row[9]))
            question_label = Label(
                scrollable_frame, text=row[0] + '.' + row[1], font='comicsans 18')
            question_label.grid(row=grid_counter, column=0, sticky='w')
            grid_counter += 1
            describe_label = Label(scrollable_frame, text='mc:' + row[7] + ', mw:' + row[8] + ', cp:' + row[9],
                                   font='14')
            describe_label.grid(row=grid_counter, column=0, sticky='w')
            grid_counter += 1
            for i in range(4):
                Radiobutton(scrollable_frame, text=row[i + 2], variable=response_list[question_counter],
                            value=str(i + 1),
                            tristatevalue='x').grid(
                    row=grid_counter, column=0, sticky='w')
                grid_counter += 1
            # response_list[question_counter] = response
            question_counter += 1
        Button(scrollable_frame, text='Submit', width=25, command=lambda: [submit(), run_quiz_frame.destroy()],
               relief=GROOVE).grid(row=grid_counter, column=1)

    run_quiz_frame.pack(fill=BOTH, expand=True)
    canvas.pack(side=LEFT, fill='both', expand=True)
    scroll_bar.pack(side='right', fill='y')

def quiz_menu(username):
    def back():
        quiz_frame.destroy()
        main_menu()

    quiz_frame = Frame(root)
    with sqlite3.connect('project1_quiz_cs384.db') as db:
        cursor = db.cursor()
    find_user = 'SELECT * FROM project1_registration WHERE username = ?'
    cursor.execute(find_user, [username])
    name_of_student = cursor.fetchall()[0][3]
    Label(quiz_frame,
          text=f"Name : {name_of_student}\nRoll : {username}", font='comicsans 18 bold').pack()
    Button(quiz_frame, text='Quiz-1', width=25, command=lambda: [run_quiz(1, username), quiz_frame.destroy()],
           relief=GROOVE).pack()
    Button(quiz_frame, text='Quiz-2', width=25, command=lambda: [run_quiz(2, username), quiz_frame.destroy()],
           relief=GROOVE).pack()
    Button(quiz_frame, text='Quiz-3', width=25, command=lambda: [run_quiz(3, username), quiz_frame.destroy()],
           relief=GROOVE).pack()

    Button(quiz_frame, text='Logout', width=20,
           command=back, relief=GROOVE).pack(pady=(25, 0))
    quiz_frame.place(relx=0.5, rely=0.5, anchor=CENTER)



root = Tk()
root.geometry("1100x300")
main_menu()
root.mainloop()

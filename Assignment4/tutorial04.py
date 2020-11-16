import re
import shutil
import os
import pandas as pd
import csv
import warnings
warnings.filterwarnings('ignore')
cwd_path = os.getcwd()
os.system('cls')
# Make sure that the file->'acad_res_stud_grades.csv' is in the 'cwd'.
# Then there would be no error.
acad_res_stud_grades_path = os.path.join(cwd_path, 'acad_res_stud_grades.csv')
grades_path = os.path.join(cwd_path, 'grades')
misc_path = os.path.join(grades_path, 'misc.csv')


def grade_converter(x):
    global grade_dict
    return grade_dict[x]


def del_create_grades_folder():
    if os.path.exists(grades_path):
        shutil.rmtree(grades_path)
        os.mkdir(grades_path)
    else:
        os.mkdir(grades_path)
    pass


del_create_grades_folder()

regex_roll = re.compile(r'\d{2}\d{2}[A-Z]{2}\d{2}')
acad_res_df = pd.read_csv(acad_res_stud_grades_path, index_col=0)
rollno_ds = acad_res_df['roll']
rollno_ds = rollno_ds.drop_duplicates()
grade_dict = {'AA': 10, 'AB': 9, 'BB': 8, 'BC': 7,
              'CC': 6, 'CD': 5, 'DD': 4, 'F': 0, 'I': 0}
grade_list = []
for grade in grade_dict:
    grade_list.append(grade)

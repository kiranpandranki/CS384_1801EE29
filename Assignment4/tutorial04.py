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

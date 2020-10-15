import shutil
import csv
import re
import os
import datetime
cwd_path = os.getcwd()
# Make sure that the file->'studentinfo_cs384.csv' is in the 'cwd'.
# Then there would be no error.
student_info_path = os.path.join(cwd_path, 'studentinfo_cs384.csv')
analytics_path = os.path.join(cwd_path, 'analytics')


def del_create_analytics_folder():
    if os.path.exists(analytics_path):
        shutil.rmtree(analytics_path)
        os.mkdir(analytics_path)
    else:
        os.mkdir(analytics_path)
    pass


def course():

    pass


def country():

    pass


def email_domain_extract():

    pass


def gender():

    pass


def dob():

    pass


def state():

    pass


def blood_group():

    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():

    pass

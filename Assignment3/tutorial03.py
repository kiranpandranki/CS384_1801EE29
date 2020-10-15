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
    # Some useful gobal variables containing important paths
    global student_info_path
    global analytics_path
    # Dictionary for stream_code and stream_name
    stream_dict = {'01': 'btech', '11': 'mtech', '12': 'msc', '21': 'phd'}
    # Creating some important paths
    course_path = os.path.join(analytics_path, 'course')
    misc_path = os.path.join(course_path, 'misc.csv')
    # Creating 'course' directory
    if os.path.exists(course_path):
        shutil.rmtree(course_path)
        os.makedirs(course_path)
    else:
        os.makedirs(course_path)
    # Reading header row in student_info_path
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.reader(studentinfo_file)
    for row in student_reader:
        field_names = row
        break
    studentinfo_file.close()
    # Regular expression for roll number
    regex_roll = re.compile(r'(\d{2})(\d{2})([A-Z]{2})(\d{2})')
    # Dictionary reading studentinfo file
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.DictReader(studentinfo_file)
    # Iterating through student_reader
    for row in student_reader:
        match = re.fullmatch(regex_roll, row['id'])
        # Logic in case of match
        if match:
            branch = match.group(3).lower()
            stream = stream_dict[match.group(2)]
            year = match.group(1)
            dir_path = os.path.join(course_path, branch, stream)
            file_name = year+'_'+branch+'_'+stream+'.csv'
            file_path = os.path.join(dir_path, file_name)
            if not os.path.exists(file_path):
                if not os.path.exists(dir_path):
                    os.makedirs(dir_path)
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerow(dict(row))
            else:
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writerow(dict(row))
        # Logic in case of no match
        else:
            if not os.path.exists(misc_path):
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writeheader()
                    misc_writer.writerow(dict(row))
            else:
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writerow(dict(row))
    pass


def country():
    # Some useful gobal variables containing important paths
    global student_info_path
    global analytics_path
    # Creating some important paths
    country_path = os.path.join(analytics_path, 'country')
    misc_path = os.path.join(country_path, 'misc.csv')
    # Creating 'country' directory
    if os.path.exists(country_path):
        shutil.rmtree(country_path)
        os.makedirs(country_path)
    else:
        os.makedirs(country_path)
    # Reading header row in studentinfo_file
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.reader(studentinfo_file)
    for row in student_reader:
        field_names = row
        break
    studentinfo_file.close()
    # Regular expression for country
    regex_country = re.compile(r'[a-zA-Z ]+')
    # Dictionary reading studentinfo_file
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.DictReader(studentinfo_file)
    # Iterating through student_reader
    for row in student_reader:
        match = re.search(regex_country, row['country'])
        # Logic in case of match
        if match:
            file_name = match.group(0).lower() + '.csv'
            file_path = os.path.join(country_path, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerow(dict(row))
            else:
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writerow(dict(row))
        # Logic in case of no match
        else:
            if not os.path.exists(misc_path):
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writeheader()
                    misc_writer.writerow(dict(row))
            else:
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writerow(dict(row))
    pass


def email_domain_extract():
    # Some useful gobal variables containing important paths
    global student_info_path
    global analytics_path
    # Creating some important paths
    email_path = os.path.join(analytics_path, 'email')
    misc_path = os.path.join(email_path, 'misc.csv')
    # Creating 'email' directory
    if os.path.exists(email_path):
        shutil.rmtree(email_path)
        os.makedirs(email_path)
    else:
        os.makedirs(email_path)
    # Reading header row in studentinfo_file
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.reader(studentinfo_file)
    for row in student_reader:
        field_names = row
        break
    studentinfo_file.close()
    # Regular expression for email
    regex_email = re.compile(
        r'^[a-zA-Z0-9.-_]+@([a-zA-Z0-9-]+)\.[a-zA-Z]+[.a-zA-Z]*$')
    # Dictionary reading studentinfo_file
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.DictReader(studentinfo_file)
    # Iterating through student_reader
    for row in student_reader:
        match = re.search(regex_email, row['email'])
        # Logic in case of match
        if match:
            file_name = match.group(1).lower()+'.csv'
            file_path = os.path.join(email_path, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerow(dict(row))
            else:
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writerow(dict(row))
        # Logic in case of no match
        else:
            if not os.path.exists(misc_path):
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writeheader()
                    misc_writer.writerow(dict(row))
            else:
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writerow(dict(row))
    pass


def gender():
    # Some useful gobal variables containing important paths
    global student_info_path
    global analytics_path
    # Creating some important paths
    gender_path = os.path.join(analytics_path, 'gender')
    misc_path = os.path.join(gender_path, 'misc.csv')
    # Creating 'gender' directory
    if os.path.exists(gender_path):
        shutil.rmtree(gender_path)
        os.makedirs(gender_path)
    else:
        os.makedirs(gender_path)
    # Reading header row in studentinfo_file
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.reader(studentinfo_file)
    for row in student_reader:
        field_names = row
        break
    studentinfo_file.close()
    # Regular expression for gender
    regex_gender = re.compile(
        r'Female|Male')
    # Dictionary reading studentinfo_file
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.DictReader(studentinfo_file)
    # Iterating through student_reader
    for row in student_reader:
        match = re.fullmatch(regex_gender, row['gender'])
        # Logic in case of match
        if match:
            file_name = match.group(0).lower()+'.csv'
            file_path = os.path.join(gender_path, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerow(dict(row))
            else:
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writerow(dict(row))
        # Logic in case of no match
        else:
            if not os.path.exists(misc_path):
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writeheader()
                    misc_writer.writerow(dict(row))
            else:
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writerow(dict(row))
    pass


def dob():
    # Some useful gobal variables containing important paths
    global student_info_path
    global analytics_path
    # Creating some important paths
    dob_path = os.path.join(analytics_path, 'dob')
    misc_path = os.path.join(dob_path, 'misc.csv')
    # Creating 'dob' directory
    if os.path.exists(dob_path):
        shutil.rmtree(dob_path)
        os.makedirs(dob_path)
    else:
        os.makedirs(dob_path)
    # Reading header row in studentinfo_file
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.reader(studentinfo_file)
    for row in student_reader:
        field_names = row
        break
    studentinfo_file.close()
    # Regular expression for dob
    regex_dob = re.compile(
        r'(\d{2})-(\d{2})-(\d{4})')
    # Creating span dictionary
    span_dict = {'1995': '1999', '2000': '2004',
                 '2005': '2009', '2010': '2014', '2015': '2020'}
    # Dictionary reading studentinfo_file
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.DictReader(studentinfo_file)
    # Iterating through student_reader
    for row in student_reader:
        match = re.fullmatch(regex_dob, row['dob'])
        day, mon, year = match.group(1), match.group(2), match.group(3)
        date_is_valid = None
        try:
            date = datetime.datetime(int(year), int(mon), int(day))
            date_is_valid = True
        except ValueError:
            date_is_valid = False
        # Logic in case of match
        if match and 1995 <= int(year) <= 2020 and date_is_valid:
            for key in span_dict:
                if int(key) <= int(year) <= int(span_dict[key]):
                    low = key
                    high = span_dict[key]
                    break
            file_name = 'bday'+'_'+low+'_'+high+'.csv'
            file_path = os.path.join(dob_path, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerow(dict(row))
            else:
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writerow(dict(row))
        # Logic in case of no match or out of range
        else:
            if not os.path.exists(misc_path):
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writeheader()
                    misc_writer.writerow(dict(row))
            else:
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writerow(dict(row))
    pass


def state():
    # Some useful gobal variables containing important paths
    global student_info_path
    global analytics_path
    # Creating some important paths
    state_path = os.path.join(analytics_path, 'state')
    misc_path = os.path.join(state_path, 'misc.csv')
    # Creating 'state' directory
    if os.path.exists(state_path):
        shutil.rmtree(state_path)
        os.makedirs(state_path)
    else:
        os.makedirs(state_path)
    # Reading header row in studentinfo_file
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.reader(studentinfo_file)
    for row in student_reader:
        field_names = row
        break
    studentinfo_file.close()
    # Regular expression for state
    regex_state = re.compile(
        r'[a-zA-Z ]+')
    # Dictionary reading studentinfo_file
    studentinfo_file = open(student_info_path, 'r')
    student_reader = csv.DictReader(studentinfo_file)
    # Iterating through student_reader
    for row in student_reader:
        match = re.search(regex_state, row['state'])
        # Logic in case of match
        if match:
            file_name = match.group(0).lower()+'.csv'
            file_path = os.path.join(state_path, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writeheader()
                    writer.writerow(dict(row))
            else:
                with open(file_path, 'a', newline='') as append_file:
                    writer = csv.DictWriter(
                        append_file, fieldnames=field_names)
                    writer.writerow(dict(row))
        # Logic in case of no match
        else:
            if not os.path.exists(misc_path):
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writeheader()
                    misc_writer.writerow(dict(row))
            else:
                with open(misc_path, 'a', newline='') as misc_file:
                    misc_writer = csv.DictWriter(
                        misc_file, fieldnames=field_names)
                    misc_writer.writerow(dict(row))
    pass


def blood_group():

    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():

    pass

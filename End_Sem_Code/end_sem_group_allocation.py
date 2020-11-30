import pandas as pd
import os
import re
import csv
import warnings
import shutil
warnings.filterwarnings('ignore')
cwd_path = os.getcwd()


def branch_strength(data_file_path, groups_path):
    master_data_frame = pd.read_csv(data_file_path)
    rollno_series = master_data_frame['Roll']
    branch_strength_dict = {}
    for x in rollno_series:
        branch_code = x[4:6]
        try:
            branch_strength_dict[branch_code] += 1
        except:
            branch_strength_dict[branch_code] = 1
    branch_strength_list = sorted(
        branch_strength_dict.items(), key=lambda item: item[0])
    branch_strength_list = sorted(
        branch_strength_list, key=lambda tup: tup[1], reverse=True)
    branch_strength_list.insert(0, ('BRANCH_CODE', 'STRENGTH'))
    branch_data_frame = pd.DataFrame(branch_strength_list)
    branch_strength_path = os.path.join(groups_path, 'branch_strength.csv')
    branch_data_frame.to_csv(branch_strength_path, index=False, header=False)
    return None


def individual_csv(data_file_path, groups_path):
    branch_path_list = []
    with open(data_file_path, 'r') as read_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            branch_file_path = os.path.join(
                groups_path, row['Roll'][4:6]+'.csv')
            if not os.path.exists(branch_file_path):
                branch_path_list.append(branch_file_path)
                with open(branch_file_path, 'a', newline='') as append_file:
                    appender = csv.DictWriter(append_file, fieldnames=[
                                              'Roll', 'Name', 'Email'])
                    appender.writeheader()
                    appender.writerow(dict(row))
            else:
                with open(branch_file_path, 'a', newline='') as append_file:
                    appender = csv.DictWriter(append_file, fieldnames=[
                                              'Roll', 'Name', 'Email'])
                    appender.writerow(dict(row))
    for branch_path in branch_path_list:
        branch_data_frame = pd.read_csv(branch_path)
        branch_data_frame.sort_values('Roll', inplace=True)
    return None


def group_allocation(filename, number_of_groups):
    data_file_path = os.path.join(cwd_path, filename)
    no_gps = number_of_groups
    groups_path = os.path.join(cwd_path, 'groups')
    if os.path.exists(groups_path):
        shutil.rmtree(groups_path)
        os.mkdir(groups_path)
    else:
        os.mkdir(groups_path)
    branch_strength(data_file_path, groups_path)
    individual_csv(data_file_path, groups_path)
    return None

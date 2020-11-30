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


def stats_grouping(number_of_groups, groups_path):
    n = number_of_groups
    if n <= 0:
        return None
    padding = 2
    list_of_list = [['group', 'total']]
    branch_strength_path = os.path.join(groups_path, 'branch_strength.csv')
    df = pd.read_csv(branch_strength_path)
    branch_list = list(df['BRANCH_CODE'])
    strength_list = [int(x) for x in list(df['STRENGTH'])]
    for x in branch_list:
        list_of_list[0].append(x)
    for i in range(1, n+1):
        if(len(str(i)) < padding):
            group_no = '0'*(padding-len(str(i))) + str(i)
        else:
            group_no = str(i)
        group_file_name = 'Group_G'+group_no+'.csv'
        list_of_list.append([group_file_name])
    left_list = []
    for x in strength_list:
        appender = int(x/n)
        left_list.append(x % n)
        for ind in range(1, n+1):
            list_of_list[ind].append(appender)
    if sum(left_list):
        start_ind2 = 1
        for ind1 in range(len(left_list)):
            for ind2 in range(start_ind2, left_list[ind1]+start_ind2):
                list_of_list[ind2 % n if ind2 % n else n][ind1+1] += 1
            start_ind2 = ind2+1
    for i in range(1, n+1):
        list_of_list[i].insert(1, sum(list_of_list[i][1:]))
    group_stats_df = pd.DataFrame(list_of_list)
    group_stats_path = os.path.join(groups_path, 'stats_grouping.csv')
    group_stats_df.to_csv(group_stats_path, header=False, index=False)
    return None


def groups_files(groups_path, n):
    group_stats_path = os.path.join(groups_path, 'stats_grouping.csv')
    branch_strength_path = os.path.join(groups_path, 'branch_strength.csv')
    try:
        group_stats_df = pd.read_csv(group_stats_path)
    except:
        return None
    branch_strength_df = pd.read_csv(branch_strength_path)
    branch_list = list(branch_strength_df['BRANCH_CODE'])
    individual_group_list = group_stats_df['group']
    for branch in branch_list:
        branch_path = os.path.join(groups_path, branch+'.csv')
        individual_branch_df = pd.read_csv(branch_path)
        members_series = group_stats_df[branch]
        start_ind = 0
        for individual_group, mem in zip(individual_group_list, members_series):
            individual_group_path = os.path.join(groups_path, individual_group)
            if not os.path.exists(individual_group_path):
                individual_branch_df.iloc[start_ind:start_ind +
                                          mem].to_csv(individual_group_path, mode='a', index=False)
            else:
                individual_branch_df.iloc[start_ind:start_ind +
                                          mem].to_csv(individual_group_path, mode='a', index=False, header=False)
            start_ind += mem
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
    stats_grouping(number_of_groups, groups_path)
    groups_files(groups_path, number_of_groups)
    return None

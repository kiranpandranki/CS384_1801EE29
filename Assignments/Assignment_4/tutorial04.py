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
for roll in rollno_ds:
    summation = 0
    file_path = os.path.join(grades_path, roll+'_individual.csv')
    temp_data_frame = acad_res_df[acad_res_df['roll'] == roll]
    match = re.fullmatch(regex_roll, roll)
    for val in temp_data_frame.isnull().sum()['sem':'credit_obtained']:
        summation += val
    grade_series = temp_data_frame['credit_obtained']
    grade_series = grade_series.drop_duplicates()
    grade_truth = set(grade_series).issubset(set(grade_list))
    sem_series = temp_data_frame['sem']
    sem_series = sem_series.drop_duplicates()
    sem_list = sorted([int(x) for x in list(sem_series)])
    sem_truth = sem_list[-1] == len(sem_list)
    temp_data_frame = temp_data_frame[[
        'sub_code', 'total_credits', 'sub_type', 'credit_obtained', 'sem']]
    if(match and not summation and grade_truth and sem_truth):
        with open(file_path, 'w', newline='') as writer_file:
            writer = csv.writer(writer_file)
            writer.writerow(['Roll: '+roll, '', '', '', ''])
            writer.writerow(['Semester Wise Details', '', '', '', ''])
        temp_data_frame.to_csv(file_path, mode='a', index=False, header=[
            'Subject', 'Credits', 'Type', 'Grade', 'Sem'])
        spi_cpi_data_frame = temp_data_frame[[
            'total_credits', 'credit_obtained', 'sem']]
        spi_cpi_data_frame['product'] = spi_cpi_data_frame['total_credits'] * \
            (spi_cpi_data_frame['credit_obtained'].apply(grade_converter))
        overall_data_frame = spi_cpi_data_frame['sem']
        overall_data_frame = pd.DataFrame(overall_data_frame)
        overall_data_frame = overall_data_frame.drop_duplicates()
        spi_list = []
        cr_list = []
        tot_cr_list = [0]
        cpi_list = []
        addition = 0.00
        for sem in sem_list:
            denominator = spi_cpi_data_frame[spi_cpi_data_frame['sem'] == sem]['total_credits'].sum(
            )
            numerator = spi_cpi_data_frame[spi_cpi_data_frame['sem'] == sem]['product'].sum(
            )
            spi = round(numerator/denominator, 2)
            spi_list.append(spi)
            cr_list.append(denominator)
            tot_cr_list.append(tot_cr_list[-1]+denominator)
        overall_data_frame['cr'] = cr_list
        overall_data_frame['cr_cl'] = cr_list
        overall_data_frame['spi'] = spi_list
        overall_data_frame['tot_cr'] = tot_cr_list[1:]
        overall_data_frame['tot_cr_cl'] = tot_cr_list[1:]
        spi_pr_list = list(
            overall_data_frame['spi']*overall_data_frame['cr_cl'])
        for x, y in zip(spi_pr_list, tot_cr_list[1:]):
            addition += x
            cpi_list.append(round(addition/y, 2))
        overall_data_frame['cpi'] = cpi_list
        with open(file_path.replace('individual.csv', 'overall.csv'), 'w', newline='') as writer_file:
            writer = csv.writer(writer_file)
            writer.writerow(['Roll: '+roll, '', '', '', ''])
        overall_data_frame.to_csv(file_path.replace('individual.csv', 'overall.csv'), mode='a', index=False, header=[
            'Semester', 'Semester Credits', 'Semester Credits Cleared', 'SPI', 'Total Credits', 'Total Credits Cleared', 'CPI'])
    else:
        with open(misc_path, 'a', newline='') as writer_file:
            writer = csv.writer(writer_file)
            writer.writerow(['Roll: '+roll, '', '', '', ''])
            writer.writerow(['Semester Wise Details', '', '', '', ''])
        temp_data_frame.to_csv(misc_path, mode='a', index=False, header=[
            'Subject', 'Credits', 'Type', 'Grade', 'Sem'])

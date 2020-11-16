
import os
import re
import csv
cwd_path = os.getcwd()
# Make sure that the folder->'Subtitles' is in the 'cwd'.
# Then there would be no error.
Subtitles_path = os.path.join(cwd_path, 'Subtitles')


def rename_FIR(folder_name):
    # rename Logic
    global Subtitles_path
    FIR_path = os.path.join(Subtitles_path, 'FIR')
    episode_pad = int(input("Enter the episode padding : "))
    regex = re.compile(r'(Episode|Ep)( )*(\d+)')
    for path, dirs, files in os.walk(Subtitles_path):
        if(path == FIR_path):
            files_list = files
            break
    for each_file in files_list:
        file_extension = each_file[-4:]
        match = re.search(regex, each_file)
        try:
            episode_num = str(int(match.group(3)))
        except:
            print('Got error in this file-->', each_file)
        if(len(episode_num) < episode_pad):
            temp = episode_pad - len(episode_num)
            episode_num = '0'*temp + episode_num
        new_file_name = 'FIR' + ' - '+'Episode '+episode_num+file_extension
        old_file_path = os.path.join(FIR_path, each_file)
        new_file_path = os.path.join(FIR_path, new_file_name)
        try:
            os.rename(old_file_path, new_file_path)
        except:
            os.remove(old_file_path)
    return None


def rename_Game_of_Thrones(folder_name):
    # rename Logic
    return None


def rename_Sherlock(folder_name):
    # rename Logic
    return None


def rename_Suits(folder_name):
    # rename Logic
    return None


def rename_How_I_Met_Your_Mother(folder_name):
    # rename Logic
    return None

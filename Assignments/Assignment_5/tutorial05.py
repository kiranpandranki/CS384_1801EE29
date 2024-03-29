
import os
import re
import csv
cwd_path = os.getcwd()
# Make sure that the folder->'Subtitles' is in the 'cwd'.
# Then there would be no error.
Subtitles_path = os.path.join(cwd_path, 'Subtitles')


def rename_FIR():
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
    print("\nFIR folder has been renamed")
    return None


def rename_Game_of_Thrones():
    # rename Logic
    global Subtitles_path
    GOT_path = os.path.join(Subtitles_path, 'Game of Thrones')
    season_pad = int(input("Enter the season padding : "))
    episode_pad = int(input("Enter the episode padding : "))
    regex = re.compile(
        r'([A-Za-z ]+)-([0-9x ]+)-([a-zA-Z ]+)')
    for path, dirs, files in os.walk(GOT_path):
        if(path == GOT_path):
            files_list = files
            break
    for each_file in files_list:
        file_extension = each_file[-4:]
        match = re.search(regex, each_file)
        episode_data = match.group(2).strip()
        season_num, episode_num = [str(int(x))
                                   for x in episode_data.split('x')]
        if(len(season_num) < season_pad):
            temp = season_pad - len(season_num)
            season_num = '0'*temp + season_num
        if(len(episode_num) < episode_pad):
            temp = episode_pad - len(episode_num)
            episode_num = '0'*temp + episode_num
        episode_title = match.group(3).strip()
        new_file_name = 'Game of Thrones' + ' - ' + 'Season ' + \
            season_num + ' Episode '+episode_num+' - '+episode_title+file_extension
        old_file_path = os.path.join(GOT_path, each_file)
        new_file_path = os.path.join(GOT_path, new_file_name)
        try:
            os.rename(old_file_path, new_file_path)
        except:
            os.remove(old_file_path)
    print("\nGame of Thrones folder has been renamed")
    return None


def rename_Sherlock():
    # rename Logic
    global Subtitles_path
    SH_path = os.path.join(Subtitles_path, 'Sherlock')
    season_pad = int(input("Enter the season padding : "))
    episode_pad = int(input("Enter the episode padding : "))
    regex = re.compile(
        r'S(\d+)\.*E(\d+)')
    for path, dirs, files in os.walk(Subtitles_path):
        if(path == SH_path):
            files_list = files
            break
    for each_file in files_list:
        file_extension = each_file[-4:]
        match = re.search(regex, each_file)
        season_num = str(int(match.group(1)))
        episode_num = str(int(match.group(2)))
        if(len(season_num) < season_pad):
            temp = season_pad - len(season_num)
            season_num = '0'*temp + season_num
        if(len(episode_num) < episode_pad):
            temp = episode_pad - len(episode_num)
            episode_num = '0'*temp + episode_num
        new_file_name = 'Sherlock' + ' - ' + 'Season ' + \
            season_num + ' Episode '+episode_num+file_extension
        old_file_path = os.path.join(SH_path, each_file)
        new_file_path = os.path.join(SH_path, new_file_name)
        try:
            os.rename(old_file_path, new_file_path)
        except:
            os.remove(old_file_path)

    print("\nSherlock folder has been renamed")
    return None


def rename_Suits():
    # rename Logic
    global Subtitles_path
    S_path = os.path.join(Subtitles_path, 'Suits')
    season_pad = int(input("Enter the season padding : "))
    episode_pad = int(input("Enter the episode padding : "))
    regex = re.compile(
        r'([A-Za-z ]+)-([0-9x ]+)-([a-zA-Z ]+)')
    for path, dirs, files in os.walk(Subtitles_path):
        if(path == S_path):
            files_list = files
            break
    for each_file in files_list:
        file_extension = each_file[-4:]
        match = re.search(regex, each_file)
        episode_data = match.group(2).strip()
        season_num, episode_num = [str(int(x))
                                   for x in episode_data.split('x')]
        if(len(season_num) < season_pad):
            temp = season_pad - len(season_num)
            season_num = '0'*temp + season_num
        if(len(episode_num) < episode_pad):
            temp = episode_pad - len(episode_num)
            episode_num = '0'*temp + episode_num
        episode_title = match.group(3).strip()
        new_file_name = 'Suits' + ' - ' + 'Season ' + \
            season_num + ' Episode '+episode_num+' - '+episode_title+file_extension
        old_file_path = os.path.join(S_path, each_file)
        new_file_path = os.path.join(S_path, new_file_name)
        try:
            os.rename(old_file_path, new_file_path)
        except:
            os.remove(old_file_path)
    print("\nSuits folder has been renamed")
    return None


def rename_How_I_Met_Your_Mother():
    # rename Logic
    global Subtitles_path
    HIMYM_path = os.path.join(Subtitles_path, 'How I Met Your Mother')
    season_pad = int(input("Enter the season padding : "))
    episode_pad = int(input("Enter the episode padding : "))
    regex = re.compile(
        r'([A-Za-z ]+)-([0-9x -]+)-([a-zA-Z ]+)')
    for path, dirs, files in os.walk(Subtitles_path):
        if(path == HIMYM_path):
            files_list = files
            break
    for each_file in files_list:
        file_extension = each_file[-4:]
        match = re.search(regex, each_file)
        episode_data = match.group(2).strip()
        x, y = episode_data.split('x')
        if(not '-' in y):
            season_num = str(int(x))
            episode_num = str(int(y))
            if(len(season_num) < season_pad):
                temp = season_pad - len(season_num)
                season_num = '0'*temp + season_num
            if(len(episode_num) < episode_pad):
                temp = episode_pad - len(episode_num)
                episode_num = '0'*temp + episode_num
        else:
            season_num = str(int(x))
            if(len(season_num) < season_pad):
                temp = season_pad - len(season_num)
                season_num = '0'*temp + season_num
            episode_num = y.split('-')
            for i in range(2):
                episode_num[i] = str(int(episode_num[i]))
                if(len(episode_num[i]) < episode_pad):
                    temp = episode_pad - len(episode_num[i])
                    episode_num[i] = '0'*temp + episode_num[i]
            episode_num = episode_num[0] + '-'+episode_num[1]
        episode_title = match.group(3).strip()
        new_file_name = 'How I Met Your Mother' + ' - ' + 'Season ' + \
            season_num + ' Episode '+episode_num+' - '+episode_title+file_extension
        old_file_path = os.path.join(HIMYM_path, each_file)
        new_file_path = os.path.join(HIMYM_path, new_file_name)
        try:
            os.rename(old_file_path, new_file_path)
        except:
            os.remove(old_file_path)
    print("\nHow I Met Your Mother folder has been renamed")
    return None


web_series_list = ['FIR', 'Game of Thrones',
                   'How I Met Your Mother', 'Sherlock', 'Suits','Exit']
option_list = []
while(True):
    print('_'*70)
    for i in range(6):
        print(f"{i+1}) "+web_series_list[i])
    option = input("Select a web series name for renaming subtitle files : ")
    if option in option_list:
        print("\nThis folder has already been renamed\nPlease select another option")
        continue
    else:
        option_list.append(option)
    if option == '1':
        try:
            rename_FIR()
        except:
            print("\nThis folder has already been renamed\nPlease select another option")
    elif option == '2':
        try:
            rename_Game_of_Thrones()
        except:
            print("\nThis folder has already been renamed\nPlease select another option")
    elif option == '3':
        try:
            rename_How_I_Met_Your_Mother()
        except:
            print("\nThis folder has already been renamed\nPlease select another option")
    elif option == '4':
        try:
            rename_Sherlock()
        except:
            print("\nThis folder has already been renamed\nPlease select another option")
    elif option == '5':
        try:
            rename_Suits()
        except:
            print("\nThis folder has already been renamed\nPlease select another option")
    elif option == '6':
        exit()
    else:
        print("Select a valid option")


"""
using os.path.join // to join the path
using os.listdir(path)
using os.rename(pathS,pathD) //move file source to destination 
"""


import os

#folder_path = r"C:\Users\deepika\Desktop\alltypefiles"
#folder_path = r"C:\Users\deepika\Desktop\movie"
folder_path = r"C:\Users\deepika\Downloads"

def folder_path_builder(path,folder_name):
    path = os.path.join(path,folder_name)
    return path

def check_folder_exist_or_create_new_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print("folder created successfully")
    else:
        print(" Folder Already exist")
    
    
audio_folder = folder_path_builder(folder_path,'AudioFiles')
check_folder_exist_or_create_new_folder(audio_folder)

video_folder = folder_path_builder(folder_path,'VideoFiles')
check_folder_exist_or_create_new_folder(video_folder)




def audioScan(folderPath):
    audio_files = []
    audio_extensions = ['mp3','m4a','aa','aac','flac']
    all_files = os.listdir(folderPath)

    for audio_extension in audio_extensions:
        for single_file in all_files:
            if audio_extension in single_file :
                audio_files.append(single_file)

    return audio_files


#audio_file_list = audioScan(folder_path)
#print(audio_file_list)

def videoScan(folderPath):
    video_files = []
    video_extensions = ['avi','mp4','mkv','mpeg','wmp','flv']
    all_files = os.listdir(folderPath)

    for video_extension in video_extensions:
        for single_file in all_files:
            if video_extension in single_file :
                video_files.append(single_file)

    return video_files


#move file in to folder
def move_file_into_folder(source_path,destination_path,lists_of_files):
    for each_file in lists_of_files:
        source_folder = folder_path_builder(source_path,each_file)
        destination_folder = folder_path_builder(destination_path,each_file)
        os.rename(source_folder,destination_folder)
    
audio_file_list = audioScan(folder_path)
move_file_into_folder(folder_path,audio_folder,audio_file_list)


video_file_list = videoScan(folder_path)
move_file_into_folder(folder_path,video_folder,video_file_list)





    

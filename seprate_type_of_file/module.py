import os

def folder_path_builder(path,folder_name):
    path = os.path.join(path,folder_name)
    return path

def check_folder_exist_or_create_new_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        print("folder created successfully")
    else:
        print(" Folder Already exist")


def audioScan(folderPath):
    audio_files = []
    audio_extensions = ['mp3','m4a','aa','aac','flac']
    all_files = os.listdir(folderPath)

    for audio_extension in audio_extensions:
        for single_file in all_files:
            if audio_extension in single_file :
                audio_files.append(single_file)

    return audio_files

def videoScan(folderPath):
    video_files = []
    video_extensions = ['avi','mp4','mkv','mpeg','wmp','flv']
    all_files = os.listdir(folderPath)

    for video_extension in video_extensions:
        for single_file in all_files:
            if video_extension in single_file :
                video_files.append(single_file)

    return video_files

def imageScan(folderPath):
    image_files = []
    image_extensions = ['jpg','JPEG','gif','png','wmp','JPG']
    all_files = os.listdir(folderPath)

    for image_extension in image_extensions:
        for single_file in all_files:
            if image_extension in single_file :
                image_files.append(single_file)

    return image_files

def PdfScan(folderPath):
    pdf_files = []
    pdf_extensions = ['pdf','PDF']
    all_files = os.listdir(folderPath)

    for pdf_extension in pdf_extensions:
        for single_file in all_files:
            if pdf_extension in single_file :
                pdf_files.append(single_file)

    return pdf_files

def exeScan(folderPath):
    exe_files = []
    exe_extensions = ['exe']
    all_files = os.listdir(folderPath)

    for exe_extension in exe_extensions:
        for single_file in all_files:
            if exe_extension in single_file :
                exe_files.append(single_file)

    return exe_files

#move file in to folder
def move_file_into_folder(source_path,destination_path,lists_of_files):
    for each_file in lists_of_files:
        source_folder = folder_path_builder(source_path,each_file)
        destination_folder = folder_path_builder(destination_path,each_file)
        os.rename(source_folder,destination_folder)

    

"""
using os.path.join // to join the path
using os.listdir(path)
using os.rename(pathS,pathD) //move file source to destination 
"""


import os
import module

#folder_path = r"C:\Users\deepika\Desktop\alltypefiles"
#folder_path = r"C:\Users\deepika\Desktop\movie"
folder_path = r"C:\Users\deepika\Downloads"


#audio file   
audio_folder = module.folder_path_builder(folder_path,'AudioFiles')
module.check_folder_exist_or_create_new_folder(audio_folder)

audio_file_list = module.audioScan(folder_path)
module.move_file_into_folder(folder_path,audio_folder,audio_file_list)

#video file
video_folder = module.folder_path_builder(folder_path,'VideoFiles')
module.check_folder_exist_or_create_new_folder(video_folder)

video_file_list = module.videoScan(folder_path)
module.move_file_into_folder(folder_path,video_folder,video_file_list)

#image files
image_folder = module.folder_path_builder(folder_path,'ImageFiles')
module.check_folder_exist_or_create_new_folder(image_folder)

image_file_list = module.imageScan(folder_path)
module.move_file_into_folder(folder_path,image_folder,image_file_list)

# pdf files
pdf_folder = module.folder_path_builder(folder_path,'PdfFiles')
module.check_folder_exist_or_create_new_folder(pdf_folder)

pdf_file_list = module.PdfScan(folder_path)
module.move_file_into_folder(folder_path,pdf_folder,pdf_file_list)


# exe files
exe_folder = module.folder_path_builder(folder_path,'exeFiles')
print(exe_folder+"--------")
module.check_folder_exist_or_create_new_folder(exe_folder)

exe_file_list = module.exeScan(folder_path)
exe_file_list.pop(0)
module.move_file_into_folder(folder_path,exe_folder,exe_file_list)






    

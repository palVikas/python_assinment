#using os module
#using os.path.join()
#using os.listdir()
#os.remove()

import os

directory_1_path = r'E:\song1'
listof_1_directory = os.listdir(directory_1_path)


directory_2_path = r'E:\song2'
listof_2_directory = os.listdir(directory_2_path)

for each_element in listof_1_directory:
    if each_element in listof_2_directory:
        common_element = os.path.join(directory_1_path ,each_element)
        os.remove(common_element)
        print(each_element+" remove successfull")

    else:
        print (each_element+" not in the list")


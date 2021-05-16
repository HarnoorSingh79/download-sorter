import os
import shutil

file_location = "C:\\Users\\Harnoor\\Downloads\\download"     # Place Where file will be picked up
target_destination = "C:\\Users\\Harnoor\\Desktop"          # Place where file will be send

file_list = os.listdir(file_location)                         # Making list of all file in download

os.chdir(target_destination)                                # Going to desktop
os.makedirs('download sorted')                              # Making folder download sorted

os.chdir(f'{target_destination}\\download sorted')          # Going inside download sorted folder

os.makedirs('zip')                                          # Making zip folder inside download sorted
os.makedirs('pdf')
os.makedirs('video')
os.makedirs('image')
os.makedirs('exe')
os.makedirs('txt')
os.makedirs('unknown')

target_destination_zip = "C:\\Users\\Harnoor\\Desktop\\download sorted\\zip"    # Target destination location
target_destination_pdf = "C:\\Users\\Harnoor\\Desktop\\download sorted\\pdf"
target_destination_video = "C:\\Users\\Harnoor\\Desktop\\download sorted\\video"
target_destination_image = "C:\\Users\\Harnoor\\Desktop\\download sorted\\image"
target_destination_exe = "C:\\Users\\Harnoor\\Desktop\\download sorted\\exe"
target_destination_txt = "C:\\Users\\Harnoor\\Desktop\\download sorted\\txt"
target_destination_unknown = "C:\\Users\\Harnoor\\Desktop\\download sorted\\unknown"

for file in file_list:
    extension_type = os.path.splitext(file)
    if extension_type[1] == '.zip':
        print('it is zip')
        shutil.move(f'{file_location}//{file}', target_destination_zip, copy_function=shutil.copy2)
    elif extension_type[1] == '.pdf':
        print('it is pdf')
        shutil.move(f'{file_location}//{file}', target_destination_pdf, copy_function=shutil.copy2)
    elif extension_type[1] == '.mp4':
        print('it is video')
        shutil.move(f'{file_location}//{file}', target_destination_video, copy_function=shutil.copy2)
    elif extension_type[1] == '.jpg' or extension_type[1] == '.jpeg' or extension_type[1] == '.png':
        print('it is image')
        shutil.move(f'{file_location}//{file}', target_destination_image, copy_function=shutil.copy2)
    elif extension_type[1] == '.exe':
        print('it is installation file')
        shutil.move(f'{file_location}//{file}', target_destination_exe, copy_function=shutil.copy2)
    elif extension_type[1] == '.txt':
        print('it is text')
        shutil.move(f'{file_location}//{file}', target_destination_txt, copy_function=shutil.copy2)
    else:
        print('it is unknown')
        shutil.move(f'{file_location}//{file}', target_destination_unknown, copy_function=shutil.copy2)

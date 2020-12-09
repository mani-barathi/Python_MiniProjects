import os, shutil

DOWNLOADS_DIR = r'C:\Users\manib\Downloads'
# changing the program directory to downloads directory
os.chdir(DOWNLOADS_DIR)

MUSIC_DIR  = r'E:\Tunes\Latest'
IMAGES_DIR = r'C:\Users\manib\Documents\images'
DOCUMENTS_DIR = r'C:\Users\manib\Documents\new'
SETUP_EXECUTABLES_DIR = r'C:\Users\manib\Downloads\setup or softwares'


def moveFile(file):
    filename, file_extension = os.path.splitext(file.lower())

    try :
        if file_extension == '.mp3':                       # checking if it is a mp3 file
            shutil.move(file,MUSIC_DIR)
            print(f'{file} --> {MUSIC_DIR}')

        elif file_extension in ['.jpg','.png','jpeg']:     # checking if it is a image file
            shutil.move(file,IMAGES_DIR)
            print(f'{file} --> {IMAGES_DIR}')

        elif file_extension in ['.doc','.docx','.pdf','.ppt','.pptx','.xlsx']:            # checking if it is a document
            shutil.move(file,DOCUMENTS_DIR)
            print(f'{file} --> {DOCUMENTS_DIR}')

        elif file_extension in ['.msi','.exe']:             # checking if it is setup or executable file
            shutil.move(file,SETUP_EXECUTABLES_DIR)
            print(f'{file} --> {SETUP_EXECUTABLES_DIR}')
    except Exception as e:
        print(e)

# os.listdir() returns all the files present in the folder
files_folders=os.listdir()

for file in files_folders:
    if os.path.isfile(file):     # if it is a file
       moveFile(file)


# try except is used in moveFile(file) to avoid any exception
# some exception which may occur are File not found, destination directory already has the file

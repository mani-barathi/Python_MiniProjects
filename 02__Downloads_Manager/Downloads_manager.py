import os,shutil

# r - raw string
downloads_dir=r'C:\Users\manib\Downloads'
# changing the program directory to downloads directory
os.chdir(downloads_dir)


# change this dictinary to your own subjects and directories
subjects={
	"csc4005":r"H:\Fall2020\Artificial_Intelligence_CSC4005" ,
	"csc1015":r"H:\Fall2020\Cryptography_CSC1015",
	"sts3103":r"H:\Fall2020\Softskills_STS3103",
	"csc4001":r"H:\Fall2020\Software_testing_CSC4001",
	"csc4002":r"H:\Fall2020\Web_Development_CSC4002"
}

# directory
music=r'E:\Tunes\Latest'
image=r'C:\Users\manib\Documents\images'


# this list has all the subject code 
subject_code=[]
# getting the key values ( subject codes from  subjects dictionary) 
for key in subjects:
    subject_code.append(key)

# print(subject_code)

# syntax for shutil.move( filename with extension , destination directory )


def move_file(file):
    file=file.lower()   # changing the file name to lowercase to avoid confusion

    if file.endswith('.mp3'):       # checking if it is a mp3 file
        shutil.move(file,music)
        print(f'{file} is a mp3')

    elif file.endswith('.jpg') or file.endswith('.png'):            # checking if it is a image file
        shutil.move(file,image)
        print(f'{file} is a image')

    elif file.endswith('.doc') or file.endswith('.docx') or file.endswith('.pdf') or file.endswith('.ppt') or file.endswith('.pptx') :
        
        if subject_code[0] in file:                         # checking if the file is realted to cryptography  
            shutil.move(file,subjects[subject_code[0]])         
            print(f'{file} ---> {subjects[subject_code[0]]}')

        elif subject_code[1] in file:
            shutil.move(file,subjects[subject_code[1]])
            print(f'{file} ---> {subjects[subject_code[1]]}')

        elif subject_code[2] in file:
            shutil.move(file,subjects[subject_code[2]])
            print(f'{file} ---> {subjects[subject_code[2]]}')

        elif subject_code[3] in file:
            shutil.move(file,subjects[subject_code[3]])
            print(f'{file} ---> {subjects[subject_code[3]]}')

        elif subject_code[4] in file:
            shutil.move(file,subjects[subject_code[4]])
            print(f'{file} ---> {subjects[subject_code[4]]}')


# os.listdir() returns all the files present in the folder
files_folders=os.listdir()


for file in files_folders:
    if os.path.isdir(file):     # if it is a folder skip the iteration 
        continue
    else:                       # if it is a file call move_file() function
        move_file(file)
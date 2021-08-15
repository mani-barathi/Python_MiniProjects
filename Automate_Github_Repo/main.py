from github import Github
import sys,os

# assuming that we have to create a folder in our computer
create_folder=True

# CURRENT_DIR is the directory where this program is stored and executed
# change This to your requirement
CURRENT_DIR=r'C:\Users\manib\Desktop\Programs\Automate_repo_creation_github'

# DIRECTORY is the directory where you want the created folder to be stored
# change This to your requirement
DIRECTORY=fr'C:\Users\manib\Documents'

# generate you token from github and replace here
TOKEN=''

try:
	if len(sys.argv)==3	:		# if we don't want to create a folder  create_folder=False
		create_folder=False		
	os.chdir(CURRENT_DIR)
	REPO_NAME=sys.argv[1]
	DIRECTORY=fr'{DIRECTORY}\{REPO_NAME}'

	g=Github(TOKEN)  		# 
	user=g.get_user()		# login and returns a user object
	USERNAME=user.login		# returns th username
	repository=user.create_repo(REPO_NAME)

except Exception as e:
	print(e)

else:
	commands=[
		'git init',
		f'git remote add origin https://github.com/{USERNAME}/{REPO_NAME}.git',
		'git add .',
		'git commit -m "Initial commit"',
		'git push -u orgin master'
	]

	if create_folder:
		
		os.mkdir(DIRECTORY)
		os.system(f'cd {DIRECTORY}')

		with open(f'{DIRECTORY}/README.MD','w') as f:
			f.write(f'#{REPO_NAME}')

	# for cmd in commands:
	# 	os.system(cmd)

	print(f'Username: {USERNAME}')
	print(f'Repository Link: https://github.com/{USERNAME}/{REPO_NAME}.git')


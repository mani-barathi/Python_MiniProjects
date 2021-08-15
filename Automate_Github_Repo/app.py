from selenium import webdriver				# pip install selenium
from selenium.webdriver.common.keys import Keys
import time

SITE=r'https://github.com/login'
SITE2=r'https://github.com/new'

# getting the details from the user 
repo_name=input("Enter a new repository name: ")
USERNAME=input("Enter Github Username: ")
PASS=input("Enter Github Password: ")

# i am using firefox as my browser if you want just change below, but make sure you have that particular webdriver
driver=webdriver.Firefox()
driver.get(SITE)

print(f'\nwe are in: {driver.current_url}')

# Sending the credentials and pressing enter
email=driver.find_element_by_id('login_field')
email.send_keys(USERNAME+Keys.TAB+PASS+Keys.ENTER)

time.sleep(2)	# just to make sure the next page is loaded

driver.get(SITE2)
print(f'we are in: {driver.current_url}')

time.sleep(2)	# just to make sure the next page is loaded

# Sending the repository name 
repo=driver.find_element_by_id('repository_name')
repo.send_keys(repo_name)

time.sleep(2)
# Clicking the create button to complete the process
createbtn=driver.find_element_by_css_selector('button.btn:nth-child(10)')
createbtn.click()

time.sleep(3)	# just to make sure the next page is loadedtime.sleep(2)

repo_url=f'{driver.current_url}.git'
print("----------------------------------------------------------------")
print(f'Repository name: {repo_name}')
print(f'Repository Url: {repo_url}')


driver.close()
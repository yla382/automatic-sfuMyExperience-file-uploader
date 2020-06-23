from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
import ast
import os


def login(usr, passw):
	username = driver.find_element_by_xpath('//*[@id="username"]')
	password = driver.find_element_by_xpath('//*[@id="password"]')
	login = driver.find_element_by_xpath('//*[@id="fm1"]/input[4]')
	username.send_keys(usr)
	password.send_keys(passw)
	login.click()


def browse():
	driver.find_element_by_xpath('//*[@id="sideMenu"]/ul/li[4]/a').click()
	driver.find_element_by_xpath('//*[@id="mainContentDiv"]/div[2]/div/div[1]/div/a[1]').click()
	driver.find_element_by_xpath('//*[@id="mainContentDiv"]/div[2]/div/a[1]').click()


def setFiles(name, val):
	file_name = driver.find_element_by_xpath('//*[@id="docName"]')
	file_name.send_keys(name)
	dropdown = Select(driver.find_element_by_id('docType'))
	dropdown.select_by_value(val)


def loadfile(file_name):
	path = os.getcwd() + '//' + file_name
	file_upload = driver.find_element_by_id('fileUpload_docUpload').send_keys(path)

def uploadfile():
	submit = driver.find_element_by_xpath('//*[@id="mainContentDiv"]/div[2]/div/a[1]')
	submit.click()



index_code = {'sis': 18, 'cl': 14, 'res': 15, 'tr': 16, 'ws': 19, 
	'ref': 22, 'wp': 30, 'other': 23, 'rep1': 20, 'rep2': 21, 'tc': 31, 'wpa': 34, 'wpr': 35}

context_file = open('contexts.txt', 'r')
context = ast.literal_eval(context_file.read())

username = context['username']
password = context['password']

file_type = index_code[sys.argv[1]]
file_name = sys.argv[2]
file_input_name = sys.argv[3]

driver = webdriver.Chrome()
driver.get('https://cas.sfu.ca/cas/login?message=Welcome+to+SFU+myExperience.%20Please+login+with+your+SFU+computing+ID.&allow=student&renew=true&service=https://myexperience.sfu.ca/sfuLogin.htm%3Faction%3Dlogin')
driver.maximize_window()

login(username, password)
browse()
setFiles(file_input_name, str(file_type))
loadfile(file_name)
time.sleep(1)
uploadfile()

driver.quit()
context_file.close()




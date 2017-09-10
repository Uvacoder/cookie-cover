#Parses the Recruit Guelph page given the URL
from selenium import webdriver
from bs4 import BeautifulSoup
import re
import json

DEBUG = True

#Log printing
def log(d):
    if DEBUG:
        print(d)

#Parsing for the address portion of the cover letter
def parseAddress(driver):
    #Get the job page
    html = driver.page_source
    bs = BeautifulSoup(html, "html.parser")
    #Find all
    tdList = bs.find_all("td", {"width":"75%"})
    #List all tds and remove all tabs and newlines
    for td in tdList:
        #Remove newlines and tabs
        td = td.get_text().strip()
        #Remove quotes
        td = re.sub("'", "", td)
        log(td.encode("utf-8"))

#Load up configs
with open('config.json') as configs:
    jsonConfigs = json.load(configs)
    log(jsonConfigs)
#Start up Chrome and get user to navigate to page
print("Starting Chrome Window...")
print("Please navigate to the job page.")
driver = webdriver.Chrome("C:/Users/Bradley/AppData/Local/Programs/Python/Python35/Scripts/chromedriver.exe")
driver.get("https://www.recruitguelph.ca/students/student-login.htm")
#Log into SSO
username = driver.find_element_by_id("inputUsername")
password = driver.find_element_by_id("inputPassword")
username.send_keys(jsonConfigs["username"])
password.send_keys(jsonConfigs["password"])
driver.find_element_by_class_name("btn").click()
#Navigate to job pages
driver.find_element_by_link_text("Co-op").click()
driver.find_element_by_link_text("Co-op Job Postings").click()

#Wait for user to be ready
ready = False
while(ready == False):
    readyAnswer = input("Are you ready? ")
    if(readyAnswer == "y" or readyAnswer == "yes"):
        ready = True
parseAddress(driver)

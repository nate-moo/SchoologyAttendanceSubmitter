import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from seleniumrequests import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

###### Info ######
username = ""
password = ""
url = ""
courseURL = url + ""
searchQuery = ""
########################

### Assigning Variables ###
listdaily = []
listElem = []
### ------------------- ###

driver = webdriver.Firefox() # Set up Web Driver - This uses Firefox
driver.get(url) # Gets page data from URL
user = driver.find_element_by_id("userNameInput") # Finds the input box with the ID of userNameInput
user.send_keys(username) # Types the input username
passwd = driver.find_element_by_id("passwordInput") # Finds the input box with the ID of passwordInput
passwd.send_keys(password) # Types the input Password
driver.find_element_by_id("submitButton").click() # Finds the submit button and clicks it
driver.get(courseURL) # Instead of navigating the page manually, we just go straight to the course page to save time
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody"))) # Waits for the lazy loaded table of assignments to load in
listOfAssignments = driver.find_elements_by_tag_name("div > a") # Finds elements with the a tag that directly follows a div tag

for i in listOfAssignments: # For loop for each item in listOfAssignments
    try: # Try, don't send an error
        if searchQuery in i.text: # Tests for if the searchQuery is contained in i.text
            listdaily.append(i.text) # if it is it's added to the listdaily List and the listElem list
            listElem.append(i)
    except: # Excepts the error if there is one
        pass # Prevents the error from stopping the code by just continuing on past it

print(listdaily[-1]) # Prints out the last element in the listdaily list
print(listElem[-1]) # Prints out the last element in the listElem list

def completeAssignment(index): # Made this a function for a future addition
    listElem[index].click() # Clicks the element described by the index
    #WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "begin-test-quiz")))
    driver.find_element_by_id("begin-test-quiz").click() # Clicks the begin test button
    #driver.find_element_by_id("edit-resume-1").click() # In case you started the quiz already
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "edit-submit"))) #waits for the test to finish loading
    driver.find_element_by_class_name("form-radio").click() # Clicks on the element that says you are here for school
    driver.find_element_by_id("edit-submit").click() # clicks the submit button
    sleep(0.25) # Waits for the modal to complete dunno why I didn't use webdriver wait, may fix that later
    driver.find_element_by_id("popup_confirm").click() # Finds and Clicks the Confirmation button in the modal

#if completeAssignment(-1) != 0: # A future addition not currently tested
#    for x in range(15):
#       if completeAssignment(-x) == 0:
#            break
#        else:
#            pass

completeAssignment(-1) # A temporary running of the function with the defualt index to be used

#driver.quit() # Quits Selenium but currently disabled incase of an error
exit() # Exits the program
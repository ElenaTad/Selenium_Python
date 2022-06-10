from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time



s = Service("c:\\browser_driver\\chromedriver.exe")
driver = webdriver.Chrome(service=s)


# Navigate to Practice page
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# Maximize the page
driver.maximize_window()

# Check if Practice page is opened
assert 'Practice Page' in driver.title

# Select Radio button 1
driver.find_element(by=By.NAME, value='radioButton').click()

# Check if first radio button is selected
assert driver.find_element(by=By.NAME, value='radioButton').is_selected

#Select from static dropdown list
driver.find_element(By.ID,"autocomplete").send_keys("Arm")
driver.implicitly_wait(10)
driver.find_element(By.ID,"ui-id-1").click()

#Select an item from dynamic dropdown list

driver.find_element(By.ID,"dropdown-class-example").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//option[@value="option1"]').click()
assert driver.find_element(By.XPATH,'//option[@value="option1"]').is_selected

#select checkbox

driver.find_element(By.ID,"checkBoxOption2").click()
assert driver.find_element(By.ID,"checkBoxOption2").is_selected()

#swith to another window

parent_handle = driver.current_window_handle
print(parent_handle)
driver.find_element(By.ID,"openwindow").click()
all_handles=driver.window_handles
print(all_handles)
for handle in all_handles:
    if handle != parent_handle:
       driver.switch_to.window(handle)
       #driver.maximize_window(handle)
       driver.find_element(By.ID,"sumome-jquery-iframe").click
       time.sleep(3)
       driver.close()
       time.sleep(2)
       break







time.sleep(5)

driver.quit()

print("Test completed")


print("URAAAA EXAV")

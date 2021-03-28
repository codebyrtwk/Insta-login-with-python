from selenium import webdriver
import time


#user inputs
user = str(input("Enter Your username"))
paswrd = str(input("Enter your password"))

#OPENING CHROME
driver = webdriver.Chrome()

#WEBSITE URL
driver.get("https://www.instagram.com/")

#hold after opening website
time.sleep(2)

#SELECTING USERNAME AND FILLING IT
username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys(user)

#SELECTING Password AND FILLING IT
password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys(paswrd)

#CLICKING LOGIN BUTTON
loginbutton = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
loginbutton.click()























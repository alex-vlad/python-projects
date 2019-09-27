from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox(executable_path=r"")
count=True 
while count==True:
  users=input("Enter your mail/account:")
  passwords=input("Enter your password:")
  driver.get("https://login.yahoo.com/")
  user=driver.find_element_by_name("username")
  user.send_keys(users)
  nextb = driver.find_element_by_name('signin')
  driver.implicitly_wait(5)
  nextb.click()
  password=driver.find_element_by_id("login-passwd")
  password.send_keys(passwords)
  nexta = driver.find_element_by_id('login-signin')
  nexta.click()
  try:
     WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"uh-as-email")))
     print("Login succesful!")
     count=False 
  except:
     print("User or password is wrong. Try again.")





        

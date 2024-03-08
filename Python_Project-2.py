#!/usr/bin/env python
# coding: utf-8

# In[75]:


##TEST_CASE-01

import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.CLASS_NAME,"orangehrm-login-forgot-header").click()
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/div/form/div[2]/button[2]').click()
time.sleep(2)
message=driver.find_element(By.CLASS_NAME,"oxd-text--p").text
print(message)


# In[72]:


##TEST_CASE-02

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
from selenium.webdriver.common.by import By
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"oxd-button").click()
print(driver.title)


# In[73]:


driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
time.sleep(2)
list=driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]')
for i in list:
    print(i.text)


# In[74]:


##TEST_CASE-03

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(4)
from selenium.webdriver.common.by import By
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"oxd-button").click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a').click()
time.sleep(2)
list=driver.find_elements(By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']")
for i in list:
    print(i.text)


# In[ ]:





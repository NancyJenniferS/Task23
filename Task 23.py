#!/usr/bin/env python
# coding: utf-8

# In[5]:


from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
chrome_service = ChromeService(r"C:\Users\Nancy\OneDrive - ZF Friedrichshafen AG\Desktop\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://jqueryui.com/droppable/")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.switch_to.frame(driver.find_element(By.CLASS_NAME,"demo-frame"))
time.sleep(3)
frame_1 = driver.find_element(By.ID,'draggable')
frame_2 = driver.find_element(By.ID,'droppable')
time.sleep(3)
action_chains = ActionChains(driver)
action_chains.drag_and_drop(frame_1,frame_2).perform()
time.sleep(3)
print("Drag and Drop done")
time.sleep(3)
driver.close()


# In[ ]:





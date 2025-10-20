import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(3)
#login
enter_username = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
enter_username.send_keys('Admin')
enter_password = driver.find_element(By.CSS_SELECTOR, '#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(3) > div > div:nth-child(2) > input')
enter_password.send_keys('admin123')
click_login_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
click_login_button.click()
time.sleep(4)


#Click Admin Module
click_admin_button = driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(1) > a > span')
click_admin_button.click()
time.sleep(3)

#Click on User Management Button
click_user_management_dropdown_button = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span')
click_user_management_dropdown_button.click()
time.sleep(2)

#Click on Job Button
click_job_dropdown_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/span')
click_job_dropdown_button.click()
time.sleep(2)

#Click on Organization Button
click_organization_dropdown_button = driver.find_element(By.CSS_SELECTOR,'#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(3) > span')
click_organization_dropdown_button.click()
time.sleep(2)

#Click on Qualification Button
click_qualification_dropdown_button = driver.find_element(By.CSS_SELECTOR, '#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(4) > span')
click_qualification_dropdown_button.click()
time.sleep(2)

#Click on Nationalities Button
click_nationalities_button = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a')
click_nationalities_button.click()
time.sleep(4)

#Click on Corporate Branding Button
click_corporate_branding_button = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[6]/a')
click_corporate_branding_button.click()
time.sleep(4)

#Click on Configuration Button
click_configuration_dropdown_button = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span')
click_configuration_dropdown_button.click()
time.sleep(2)

#Click on User Profile Button
click_user_profile_button = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/p')
click_user_profile_button.click()
time.sleep(2)

#Click on Logout button
click_logout_button = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a')
click_logout_button.click()
time.sleep(4)

driver.quit()

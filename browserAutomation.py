import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://resources.portal.at/appcall_registration/?appid=PRM&portal=FP2&appurl=https://prm2pj.portal.at/SSOREDIRECT/REDIRECT.JSP?TO=HTTPS://PRM2PA.PORTAL.AT/nwbc")

linkElement = driver.find_element(By.LINK_TEXT, 'Alternative Anmeldemethoden').click()
time.sleep(1)

# select id austria
linkElement = driver.find_element(By.ID, 'startIdAustria').click()
time.sleep(1)

# select id austria again
linkElement = driver.find_element(By.ID, 'buttonEid').click()
time.sleep(1)

# insert values for id austria

driver.switch_to.frame(1)
print("todo - save mobile number and password safely")
driver.find_element(By.ID, "firstFactorId").send_keys("mobile_number")
driver.find_element(By.ID, "signaturpasswort").send_keys("signature_password")
driver.find_element(By.ID, "signaturpasswort").send_keys(Keys.ENTER)
time.sleep(20)
driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(1) span").click()
time.sleep(5)

# select "Startseite" menu entry
driver.find_element(By.ID, "shellAppTitle-button").click()

# select "cats erfassen"
driver.find_element(By.ID, "__label0-allMyAppsView--oItemsContainerlist-0-bdi").click()

# if it is the first day of the week - add rows for leistungsarten

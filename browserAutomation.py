import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def createArbeitsvorrateAndLeistungsarten(driver):
    # add Arbeitsvorräte
    driver.find_element(By.ID, "WD0186").click()
    driver.find_element(By.ID, "WD04C6").click()
    driver.find_element(By.ID, "WD0186").click()
    driver.find_element(By.ID, "WD05FB").click()
    driver.find_element(By.ID, "WD0186").click()
    driver.find_element(By.ID, "WD0737").click()
    driver.find_element(By.ID, "WD0186").click()
    driver.find_element(By.ID, "WD087A").click()
    # set Leistungsartens
    driver.find_element(By.ID, "WD02E1").click()
    driver.find_element(By.ID, "WD02E1").send_keys("BXACIB")
    driver.find_element(By.ID, "WD02E1").send_keys(Keys.ENTER)
    driver.find_element(By.ID, "WD031A").send_keys(Keys.DOWN)

    driver.find_element(By.ID, "WD031A").click()
    driver.find_element(By.ID, "WD031A").send_keys("BXACIB")
    driver.find_element(By.ID, "WD031A").send_keys(Keys.ENTER)
    driver.find_element(By.ID, "WD031A").send_keys(Keys.DOWN)

    driver.find_element(By.ID, "WD0353").click()
    driver.find_element(By.ID, "WD0353").send_keys("BXACIB")
    driver.find_element(By.ID, "WD0353").send_keys(Keys.ENTER)
    driver.find_element(By.ID, "WD0353").send_keys(Keys.DOWN)

    driver.find_element(By.ID, "WD038C").click()
    driver.find_element(By.ID, "WD038C").send_keys("BXACIB")
    driver.find_element(By.ID, "WD038C").send_keys(Keys.ENTER)
    # driver.find_element(By.ID, "WD031A").send_keys(Keys.DOWN)


# Monday
mondayConfig = {'hoursFieldList': ["WD021A", "WD025F", "WD02A4", "WD02E7"],
                'detailsFieldList': ["WD021E", "WD0263", "WD02A8", "WD064D"],
                'textAreaFieldList': ["WD085B", "WD0A3E", "WD0C21", "WD0E04"],
                'okButtonFieldList': ["WD085D", "WD0A40", "WD0C23", "WD0E06"]}
# Tuesday
tuesdayConfig = {'hoursFieldList': ["WD0222", "WD0267", "WD02AC", "WD02ED"],
                 'detailsFieldList': ["WD0226", "WD026B", "WD02B0", "WD0650"],
                 'textAreaFieldList': ["WD0FE7", "WD11CA", "WD13AD", "WD1590"],
                 'okButtonFieldList': ["WD0FE9", "WD11CC", "WD13AF", "WD1592"]}
# Wednesday
wednesdayConfig = {'hoursFieldList': ["WD022A", "WD026F", "WD02B4", "WD02F3"],
                   'detailsFieldList': ["WD022E", "WD0273", "WD02B8", "WD0653"],
                   'textAreaFieldList': ["WD1773", "WD1956", "WD1BCD", "WD1DB0"],
                   'okButtonFieldList': ["WD1775", "WD1958", "WD1BCF", "WD1DB2"]}
# Thursday
thursdayConfig = {'hoursFieldList': ["WD0232", "WD0277", "WD02BC", "WD02F9"],
                  'detailsFieldList': ["WD0236", "WD027B", "WD02C0", "WD0656"],
                  'textAreaFieldList': ["WD1F93", "WD2176", "WD2359", "WD253C"],
                  'okButtonFieldList': ["WD1F95", "WD2178", "WD235B", "WD253E"]}
# Friday
fridayConfig = {'hoursFieldList': ["WD023A", "WD027F", "WD02C4", "WD02FF"],
                'detailsFieldList': ["WD023E", "WD0283", "WD02C8", "WD0659"],
                'textAreaFieldList': ["", "", "", ""],  # TODO fill with values
                'okButtonFieldList': ["", "", "", ""]} # TODO fill with values

def createBookingsForDay(driver, dayConfig):
    for field in dayConfig['hoursFieldList']:
        driver.find_element(By.ID, field).send_keys("1")  # .click()

    # Prüfen Button
    driver.find_element(By.ID, "WD018F").click()

    i = 0
    for elem in dayConfig['detailsFieldList']:
        driver.find_element(By.ID, dayConfig['detailsFieldList'][i]).click()
        driver.find_element(By.ID, dayConfig['textAreaFieldList'][i]).send_keys("text for text area")
        driver.find_element(By.ID, dayConfig['okButtonFieldList'][i]).click()

driver = webdriver.Firefox()
driver.get(
    "https://resources.portal.at/appcall_registration/?appid=PRM&portal=FP2&appurl=https://prm2pj.portal.at/SSOREDIRECT/REDIRECT.JSP?TO=HTTPS://PRM2PA.PORTAL.AT/nwbc")

driver.find_element(By.LINK_TEXT, 'Alternative Anmeldemethoden').click()
time.sleep(2)

# select id austria
driver.find_element(By.ID, 'startIdAustria').click()
time.sleep(2)

# select id austria again
driver.find_element(By.ID, 'buttonEid').click()
time.sleep(2)

# insert values for id austria

driver.switch_to.frame(1)
print("todo - save mobile number and password safely")
driver.find_element(By.ID, "firstFactorId").send_keys("phone_no")
driver.find_element(By.ID, "signaturpasswort").send_keys("signature_password")
driver.find_element(By.ID, "signaturpasswort").send_keys(Keys.ENTER)
time.sleep(15)
driver.switch_to.default_content()
driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(1) span").click()
time.sleep(5)

# select "Startseite" menu entry
driver.find_element(By.ID, "shellAppTitle-button").click()
time.sleep(2)
# select "cats erfassen"
driver.find_element(By.ID, "__label0-allMyAppsView--oItemsContainerlist-0-bdi").click()
time.sleep(10)

# if it is the first day of the week - add rows for leistungsarten
noOfTheWeek = datetime.now().weekday()

# "Nächste Periode" Button
# driver.find_element(By.ID, "WD017C").click()

match noOfTheWeek:
    case 1:
        createArbeitsvorrateAndLeistungsarten(driver)
        createBookingsForDay(driver, mondayConfig)
    case 2:
        createBookingsForDay(driver, tuesdayConfig)
    case 3:
        createBookingsForDay(driver, wednesdayConfig)
    case 4:
        createBookingsForDay(driver, thursdayConfig)
    case 5:
        createBookingsForDay(driver, fridayConfig)



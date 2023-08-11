import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Util.Globals import mondayConfig, tuesdayConfig, wednesdayConfig, thursdayConfig, fridayConfig


class CATsHandler:
    def __init__(self, leistungsArt):
        self.leistungArt = leistungsArt
        # driver = webdriver.Firefox()
        #self.driver = webdriver.Chrome()

    def createArbeitsvorrateAndLeistungsarten(self):
        # add Arbeitsvorräte
        self.driver.find_element(By.ID, "WD0186").click()
        self.driver.find_element(By.ID, "WD04C6").click()
        self.driver.find_element(By.ID, "WD0186").click()
        self.driver.find_element(By.ID, "WD05FB").click()
        self.driver.find_element(By.ID, "WD0186").click()
        self.driver.find_element(By.ID, "WD0737").click()
        self.driver.find_element(By.ID, "WD0186").click()
        self.driver.find_element(By.ID, "WD087A").click()
        # set Leistungsarten
        self.driver.find_element(By.ID, "WD02E1").click()
        self.driver.find_element(By.ID, "WD02E1").send_keys("BXACIB")
        self.driver.find_element(By.ID, "WD02E1").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "WD031A").send_keys(Keys.DOWN)

        self.driver.find_element(By.ID, "WD031A").click()
        self.driver.find_element(By.ID, "WD031A").send_keys("BXACIB")
        self.driver.find_element(By.ID, "WD031A").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "WD031A").send_keys(Keys.DOWN)

        self.driver.find_element(By.ID, "WD0353").click()
        self.driver.find_element(By.ID, "WD0353").send_keys("BXACIB")
        self.driver.find_element(By.ID, "WD0353").send_keys(Keys.ENTER)
        self.driver.find_element(By.ID, "WD0353").send_keys(Keys.DOWN)

        self.driver.find_element(By.ID, "WD038C").click()
        self.driver.find_element(By.ID, "WD038C").send_keys("BXACIB")
        self.driver.find_element(By.ID, "WD038C").send_keys(Keys.ENTER)
        # self.driver.find_element(By.ID, "WD031A").send_keys(Keys.DOWN)

        def createBookingsForDay(dayConfig, catsRow):
            # TODO introduce catsRow to loop through
            for field in dayConfig['hoursFieldList']:
                self.driver.find_element(By.ID, field).click()
                time.sleep(1)
                # select twice - as dom changes due to first click (id is reassigned from a span to an input field)
                self.driver.find_element(By.ID, field).send_keys()  # .click()

            # Prüfen Button
            self.driver.find_element(By.ID, "WD018F").click()

            i = 0
            for elem in dayConfig['detailsFieldList']:
                self.driver.find_element(By.ID, dayConfig['detailsFieldList'][i]).click()
                self.driver.find_element(By.ID, dayConfig['textAreaFieldList'][i]).send_keys("text for text area")
                self.driver.find_element(By.ID, dayConfig['okButtonFieldList'][i]).click()

    def signIntoCATS(self):
        self.driver.get(
            "https://resources.portal.at/appcall_registration/?appid=PRM&portal=FP2&appurl=https://prm2pj.portal.at/SSOREDIRECT/REDIRECT.JSP?TO=HTTPS://PRM2PA.PORTAL.AT/nwbc")

        self.driver.find_element(By.LINK_TEXT, 'Alternative Anmeldemethoden').click()
        time.sleep(2)

        # select id austria
        self.driver.find_element(By.ID, 'startIdAustria').click()
        time.sleep(2)

        # select id austria again
        self.driver.find_element(By.ID, 'buttonEid').click()
        time.sleep(3)

        # insert values for id austria

        self.driver.switch_to.frame(0)
        # TODO save mobile number and password safely
        self.driver.find_element(By.ID, "firstFactorId").send_keys("+436601427666")
        self.driver.find_element(By.ID, "signaturpasswort").send_keys("nw|x4rLOUK=Lv6|:o5pC")
        self.driver.find_element(By.ID, "signaturpasswort").send_keys(Keys.ENTER)
        time.sleep(15)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, ".list-group-item:nth-child(1) span").click()
        time.sleep(5)

    def moveToCATsCaptureViaMenu(self):
        # select "Startseite" menu entry
        self.driver.find_element(By.ID, "shellAppTitle-button").click()
        time.sleep(2)
        # select "cats erfassen"
        self.driver.find_element(By.ID, "__label0-allMyAppsView--oItemsContainerlist-0-bdi").click()
        time.sleep(10)

    def createBookings(self, bookingDate, catsRow):
        # if it is the first day of the week - add rows for leistungsarten
        noOfTheWeek = bookingDate.weekday()

        # "Nächste Periode" Button
        # driver.find_element(By.ID, "WD017C").click()

        match noOfTheWeek:
            case 0:
                self.createArbeitsvorrateAndLeistungsarten()
                dayConfig = mondayConfig
            case 1:
                dayConfig = tuesdayConfig
            case 2:
                dayConfig = wednesdayConfig
            case 3:
                dayConfig = thursdayConfig
            case 4:
                dayConfig = fridayConfig

        self.createBookingsForDay(dayConfig, catsRow)
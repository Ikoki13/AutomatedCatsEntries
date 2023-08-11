import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from Classes.CATsHandler import CATsHandler



catsHandler = CATsHandler("BXACIB")

catsHandler.signIntoCATS()

catsHandler.moveToCATsCaptureViaMenu()

catsHandler.createBookings(datetime.now())





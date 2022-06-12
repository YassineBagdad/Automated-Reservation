from main.selenium_folder import functions
from datetime import time
from selenium import webdriver

def main():
    
    functions.launchPlatform()

    country = 'Morocco'
    city = 'Casablanca'
    building = 'ALQUODS'
    floor = 'SHORE 16 FLOOR 1'
    functions.selectRegion(country,city,building,floor)

    #b = time1(11, 34, 56)
    #print("b =", b)
    inTime = time(8,00)
    outTime = time(17,00)
    functions.chooseTime(inTime,outTime)

    daysToBook = ("Tuesday","Wednesday","Thursday")
    functions.selectDays(daysToBook)

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
from selenium.webdriver.support.ui import Select
import datetime
from datetime import time as time1
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions

#class="mat-focus-indicator mat-button mat-button-base"
#class="mat-focus-indicator btn btn-primary mat-button mat-button-base"

#global driver

PATH = "C:\Program Files (x86)\chromedriver.exe"


def launchPlatform():
    
    global driver

    #window_before = driver.window_handles[0]


    driver = webdriver.Chrome(PATH)
    driver.get("https://hoteling.capgemini.com/reservationContent/newReservation")

    # window_after = driver.window_handles[0]
    # driver.switch_to.window(window_after)

    time.sleep(5)
    print (-1)
    try:
        
        useMapButton = WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="mat-dialog-0"]/app-google-maps-user-consent-dialog/div/div[2]/div[2]/mat-dialog-actions/button'))
        )
        useMapButton.click()
        """
        element = WebDriverWait(driver,20).until(
            EC.presence_of_element_located((By.XPATH,'//*[@id="mat-dialog-0"]/app-google-maps-user-consent-dialog/div/div[2]/div[2]/mat-dialog-actions/button').click()))
        """
        #   
        #useMapButton = driver.find_element(By.XPATH,'//*[@id="mat-dialog-0"]/app-google-maps-user-consent-dialog/div/div[2]/div[2]/mat-dialog-actions/button').click()
    except:
        print("error pressing the button")

def selectRegion(country,city,building,floor):

    selectCountry = Select(driver.find_element(By.ID,'country'))
    selectCountry.select_by_visible_text(country)

    driver.implicitly_wait(10)

    selectcity = Select(driver.find_element(By.NAME,'city'))
    selectcity.select_by_visible_text(city)


    selectbuilding = Select(driver.find_element(By.NAME,'building'))
    selectbuilding.select_by_visible_text(building)

    selectfloor = Select(driver.find_element(By.ID,'floor'))
    selectfloor.select_by_visible_text(floor)

        
        #org = driver.find_element_by_xpath('//a[@class="cbtn--s"]')
        #val = org.get_attribute("href")

    """
    //*[@id="datePickerDesk"]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td[1]
    //*[@id="datePickerDesk"]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td[2]
    //*[@id="datePickerDesk"]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td[3]
    //*[@id="datePickerDesk"]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td[4]
    """
"""
    """"""
    try:
        selectCity = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "city"))
        )
        print (-4)

    finally:
        time.sleep(5)

        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "city"))
        #//---------use other element locators too like xpath/css_selector/css_name
            )
        finally:
            select_city = Select(element)
            select_city.select_by_visible_text("Casablanca") 




            #selectCountry = driver.find_element(By.NAME,'city')
            #selectCountry = Select(driver.find_element(By.NAME,'city'))
            #selectCountry.select_by_visible_text('Casablanca')

            city = driver.find_element_by_css_selector("#city_id")
            wait = WebDriverWait(driver, 10)
            city_dropDown = wait.until(EC.visibility_of_element_located(city))
            select_city = Select(city_dropDown)
            select_city.select_by_visible_text("Moscow") 

            print (3)
            wait = WebDriverWait(driver, 10)
            city_dropDown = wait.until(EC.visibility_of_element_located(selectCountry))
            select_city = Select(city_dropDown)
            select_city.select_by_visible_text("Casablanca") 
            #driver.find_elements_by_css_selector("div[class='value test']")
            #element=wait.until(EC.element_to_be_selected(Select(driver.find_element(By.NAME,'city'))))
            #element=wait.until(EC.element_to_be_selected(driver.find_element_by_css_selector('#city > option.ng-star-inserted')))
            #select_city = Select(element)
            #select_city.select_by_visible_text("Casablanca")
            #selectCountry = Select(driver.find_element(By.ID,'city'))
            #wait.until(EC.element_to_be_selected('Casablanca')) #selectCountry.select_by_visible_text('Casablanca'))
            
            
            selectCountry = Select(driver.find_element(By.NAME,'building'))
            selectCountry.select_by_visible_text('ALQUODS')

            selectCountry = Select(driver.find_element(By.ID,'floor'))
            selectCountry.select_by_visible_text('SHORE 16 FLOOR 3')
    

            wait = WebDriverWait(driver, 10)
            element=wait.until(EC.element_to_be_selected(driver.find_element_by_css_selector('#city > option.ng-star-inserted')))
            select_city = Select(element)
            select_city.select_by_visible_text("Casablanca")
"""

"""
            select_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, '#city > option.ng-star-inserted')))
            select = Select(select_element)
            select.select_by_visible_text('Casablanca')
"""
            #print (-5)
            #selectCity.select_by_visible_text('Casablanca')

#listProducts = driver.find_element(By.CLASS_NAME,"list__products")


#  yes Button
#//*[@id="mat-dialog-0"]/app-google-maps-user-consent-dialog/div/div[2]/div[2]/mat-dialog-actions/button
#  no Button
#//*[@id="mat-dialog-0"]/app-google-maps-user-consent-dialog/div/div[2]/div[1]/mat-dialog-actions/button


def selectDays(daysToBook = []):
    weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
    weekDayInt = -1
    weeknumber = -1
    #daysToBook = ("Tuesday","Wednesday","Thursday")
    #print(10)
    todayElement = driver.find_element(By.CLASS_NAME,'today')
    todayDateString = todayElement.get_attribute("data-day")
    todayDate = datetime.datetime.strptime(todayDateString, '%m/%d/%Y').date()
    #print(todayDate)
    #thisWeek = todayElement.find_element(By.XPATH,'..')
    #weekDays = thisWeek.find_elements_by_xpath(".//*")
    calender = todayElement.find_element(By.XPATH,'../..')
    weeks = calender.find_elements(By.XPATH,".//tr")

    # thisWeekRank = 0
    # for i in weeks:
    #     thisWeekRank = thisWeekRank + 1
    #     try:
    #         dayyy = i.find_element(By.XPATH,'.//td[@class="day"]')
    #         print(dayyy.get_attribute("data-day"))
    #         #if (i.find_element(By.XPATH,'.//td[@class="day today"]')==True ): #.//td[@class="day today"]
    #         #    print("thisWeekRank : "+thisWeekRank)
    #     finally:
    #         print(-1)

    #twoWeeks = weeks.
    #print(thisWeek.get_attribute("data-day"))
    
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="datePickerDesk"]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td[3]'))).click()
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="datePickerDesk"]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td[4]'))).click()
    #days = i.find_elements(By.XPATH,".//td")
    #test1 = driver.find_element(By.XPATH,'//*[@id="datePickerDesk"]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td[3]')
    #test2 = driver.find_element(By.XPATH,'//*[@id="datePickerDesk"]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td[4]')
    #test1.click()
    #test2.click()
    #for i in weekDays:
    #    print(i.get_attribute("data-day"))
    
    bookDays =[]
    for i in weeks:
        weekDayInt = -1
        days = i.find_elements(By.XPATH,".//td")
        for j in days:
            #thisDayRefresh = i.
            weekDayInt = weekDayInt+1
            #dayElement = driver.find_element(By.CLASS_NAME,'day')
            #day = j.find_element(By.XPATH,".//td")
            dayDateString = j.get_attribute("data-day")
            dayDate = datetime.datetime.strptime(dayDateString, '%m/%d/%Y').date()
            #print(j)
            
            if( todayDate < dayDate and weekDays[weekDayInt] in daysToBook and todayDate + datetime.timedelta(days=15) > dayDate): #and daysToBook.index(weekDays[weekDayInt]""""""daysToBook.index(weekDays[weekDayInt])
                weeknumber = weeknumber +1
                bookDays.append(j.get_attribute("data-day"))# i
                #print(weekDays[weekDayInt])
                """var = j.get_attribute("data-day")
                print(j.get_attribute("data-day"))
                print(j)
                xpath = '//td[@data-day="%s"]' %var
                var2 = driver.find_element(By.XPATH,xpath)
                var2.click()
                """#driver.click()
                #driver.find_element(By.XPATH,'//td[@data-day="'+ i.get_attribute("data-day") +'"]' ).click()
                #driver.refresh()
                #print(i.get_attribute("data-day"))
                
                #bookDay.click()
                #time.sleep(3)
                #print(type(bookDay))
                #print(i.get_attribute("data-day"))
        #print(len(bookDays))
    #etc = 3
    #select = driver.find_element(By.XPATH,'//td[@data-day="05/18/2022"]').click()
    for j in bookDays:
        xpath = '//td[@data-day="%s"]' %j
        dayy = driver.find_element(By.XPATH,xpath)
        dayy.click()
        #etc = 3
        #val = j.get_attribute("data-day")
        #select = driver.find_element(By.XPATH,'//td[@data-day="05/18/2022"]')
        #ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)
        #your_element = WebDriverWait(driver, 20,ignored_exceptions=ignored_exceptions)\
        #                        .until(expected_conditions.presence_of_element_located((By.XPATH, '//td[@data-day="'+ j.get_attribute("data-day") +'"]'))).click()

        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//td[@data-day="'+ bookDays[j].get_attribute("data-day") +'"]' ))).click()
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//td[@data-day="05/18/2022"]' ))).click()
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//td[@data-day="05/19/2022"]' ))).click()
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//td[@data-day="05/20/2022"]' ))).click()
        #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="datePickerDesk"]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td['+ str(etc) +']'))).click()
        #etc = etc+1
        #j.click()
        #//*[@id="datePickerDesk"]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td[3]
        #/html/body/app-root/main/div/div/div/app-reservation-content/div[1]/div/div[3]/div/app-new/div/div[1]/div[2]/div/div[1]/div/div[2]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td[3]
            
        

    #print(todayDate)
    #date_time_obj = datetime.datetime.strptime(date_time_str, '%m/%d/%y')
    """day = today.get_attribute("data-day")
    todayDate = datetime.datetime
    thisWeek = today.find_element_by_xpath('..')
    weekDays = thisWeek.find_elements_by_xpath(".//*")

    for i in weekDays:
    """
    #day = today.get_attribute("data-day")
    #xpathString = today.get_xpath()


    #val = today.get_attribute("data-day")
    #val = today.get_property("xpath")
    #print(today)

def chooseTime(inTime,outTime):
    #print(inTime.hour)
    #print(inTime.strftime("%H"))
    driver.implicitly_wait(10)
    inTimeDiv = driver.find_element(By.XPATH,'/html/body/app-root/main/div/div/div/app-reservation-content/div[1]/div/div[3]/div/app-new/div/div[1]/div[2]/div/div[2]/div[2]/div/div')
    inTimeHour = inTimeDiv.find_element(By.XPATH,'/html/body/app-root/main/div/div/div/app-reservation-content/div[1]/div/div[3]/div/app-new/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/ul/li[2]/div/div[1]/table/tr[2]/td[1]/span').click()
    inTimeHour = inTimeDiv.find_element(By.XPATH,'//td[text()="'+ inTime.strftime("%H") +'"][@class="hour"]').click()
    inTimeMinute = inTimeDiv.find_element(By.XPATH,'/html/body/app-root/main/div/div/div/app-reservation-content/div[1]/div/div[3]/div/app-new/div/div[1]/div[2]/div/div[2]/div[2]/div/div/div/div/ul/li[2]/div/div[1]/table/tr[2]/td[3]/span').click()
    inTimeMinute1 = inTimeDiv.find_element(By.XPATH,'//td[text()="'+ inTime.strftime("%M") +'"][@class="minute"]').click()

    #driver.execute_script("arguments[0].click();", inTimeMinute1)

    outTimeDiv = driver.find_element(By.XPATH,'/html/body/app-root/main/div/div/div/app-reservation-content/div[1]/div/div[3]/div/app-new/div/div[1]/div[2]/div/div[2]/div[3]/div/div')
    outTimeHour = outTimeDiv.find_element(By.XPATH,'/html/body/app-root/main/div/div/div/app-reservation-content/div[1]/div/div[3]/div/app-new/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div/ul/li[2]/div/div[1]/table/tr[2]/td[1]/span').click()
    #print(outTime.strftime("%H"))
    outTimeHourParent = driver.find_element(By.XPATH,'/html/body/app-root/main/div/div/div/app-reservation-content/div[1]/div/div[3]/div/app-new/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div/ul/li[2]/div/div[2]/table')
    outTimeHour = outTimeHourParent.find_element(By.XPATH,'.//td[text()="'+ outTime.strftime("%H") +'"][@class="hour"]').click()

    #outTimeHour = outTimeDiv.find_element(By.XPATH,'//td[text()="'+ outTime.strftime("%H") +'"][@class="hour"][@data-action="selectHour"]').click()
    outTimeMinute = outTimeDiv.find_element(By.XPATH,'/html/body/app-root/main/div/div/div/app-reservation-content/div[1]/div/div[3]/div/app-new/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div/ul/li[2]/div/div[1]/table/tr[2]/td[3]/span').click()
    
    outTimeMinuteParent = driver.find_element(By.XPATH,'/html/body/app-root/main/div/div/div/app-reservation-content/div[1]/div/div[3]/div/app-new/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div/ul/li[2]/div/div[3]/table')
    outTimeMinute1 = outTimeMinuteParent.find_element(By.XPATH,'.//tr/td[text()="'+ outTime.strftime("%M") +'"][@class="minute"]').click()

    #outTimeDiv = driver.find_element(By.CLASS_NAME,'col-md-8 inOutTime ng-valid ng-touched ng-dirty')

#/html/body/app-root/main/div/div/div/app-reservation-content/div[1]/div/div[3]/div/app-new/div/div[1]/div[2]/div/div[2]/div[3]/div/div/div/div/ul/li[2]/div/div[1]/table/tr[2]
#//td[text()="08"]
#//tr[text()="08"]

def chooseDesk():
    return





# if __name__=="__main__":

#     #def allFunctions():

#     launchPlatform()

#     country = 'Morocco'
#     city = 'Casablanca'
#     building = 'ALQUODS'
#     floor = 'SHORE 16 FLOOR 1'
#     selectRegion(country,city,building,floor)

#     #b = time1(11, 34, 56)
#     #print("b =", b)
#     inTime = time1(8,00)
#     outTime = time1(17,00)
#     chooseTime(inTime,outTime)

#     daysToBook = ("Tuesday","Wednesday","Thursday")
#     selectDays(daysToBook)
    #//*[@id="datePickerDesk"]/div/ul/li[1]/div/div[1]/table/tbody/tr[4]/td[2]
    
    #allFunctions()
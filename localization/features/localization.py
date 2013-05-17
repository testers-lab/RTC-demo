import time
from selenium.webdriver.common.by import By
from lettuce import step

ZIP_FIELD = (By.ID, "zipSearchQuery")
GET_STATIONS = (By.ID, "getStations")


@step('I am on the localization page')
def go_to_localization_page(step):
    driver.get("http://m.video.pbs.org")
    time.sleep(3)


@step('When I enter (.*) zipcode')
def enter_zipcode(step, zipcode):
    driver.send_keys(ZIP_FIELD, zipcode)
    driver.click(GET_STATIONS)
    time.sleep(3)


@step('I select (.*) station')
def select_station(step, station):
    STATION_SELECTED = (BY.PARTIAL_LINK_TEXT, station)
    
    try:
        driver.click(STATION_SELECTED)
        time.sleep(5)
    except:
        assert 0, "Cannot find station %s" % station

        
@step('I am able to see TV Schedule for this station')
def verify_schedule(step):
    driver.get("http://m.video.pbs.org/schedules")

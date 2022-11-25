from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementNotInteractableException
import time

def test_scenario2():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get("https://www.nlb.gov.sg/main/home")

    title = driver.title
    assert title == "Home"

    driver.implicitly_wait(0.5)

    time.sleep(1)

    nav_button = driver.find_element(by=By.ID, value="discover-menu-name-198")
    
    home_window = driver.current_window_handle
    
    try:
        nav_button.click()
    except ElementNotInteractableException:
        nav_button = driver.find_element(by=By.CLASS_NAME, value="fa.fa-bars")
        nav_button.click()
        nav_button = driver.find_element(by=By.ID, value="discover-menu-name-198")
        nav_button.click()
        
    time.sleep(1)
   
    driver.quit()

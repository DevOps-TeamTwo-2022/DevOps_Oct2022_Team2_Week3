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

    nav_button = driver.find_element(by=By.ID, value="discover-menu-name-80")
    
    home_window = driver.current_window_handle
    
    try:
        nav_button.click()
    except ElementNotInteractableException:
        nav_button = driver.find_element(by=By.CLASS_NAME, value="fa.fa-bars")
        nav_button.click()
        nav_button = driver.find_element(by=By.ID, value="discover-menu-name-80")
        nav_button.click()
        
    time.sleep(1)
    
    text_box = driver.find_element(by=By.ID, value="inputKeyword")

    submit_button = driver.find_element(By.CLASS_NAME, "form-group.col-md-1.button-group.p-0.text-center")

    text_box.send_keys("Programming")        
    
    time.sleep(1)
    
    submit_button.click()  
    
    time.sleep(5)  
    
    driver.quit()
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_scenario1():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()))

    driver.get("https://www.nlb.gov.sg/main/home")

    title = driver.title
    assert title == "Home"

    driver.implicitly_wait(0.5)

    time.sleep(2)

    text_box = driver.find_element(by=By.ID, value="searchBox")

    submit_button = driver.find_element(By.CLASS_NAME, "btn.btn-primary.height50")

    text_box.send_keys("Selenium")
    time.sleep(2)

    original_window = driver.current_window_handle
    
    submit_button.click()
    
    time.sleep(2)

    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break    

    time.sleep(2)

    message = driver.find_element(by=By.ID, value="query").get_attribute("value")
    
    value = message
    
    time.sleep(2)
    assert value == "Selenium"

    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService


options = Options()
options.page_load_strategy = 'normal'  
service = ChromeService()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://uitestingplayground.com/ajax")
    blue_button = driver.find_element(By.ID, 'ajaxButton')
    blue_button.click()
    wait = WebDriverWait(driver, 100)
    green_block = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.bg-success'))
    )
    text_from_green_block = green_block.text.strip()
    print(text_from_green_block)
finally:
    driver.quit()
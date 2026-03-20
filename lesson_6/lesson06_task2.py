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
    driver.get('http://uitestingplayground.com/textinput')
    input_field = driver.find_element(By.TAG_NAME, 'input')
    input_field.send_keys('SkyPro')
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))
    )
    button.click()
    result_text = button.text
    print(result_text)
finally:
    driver.quit()
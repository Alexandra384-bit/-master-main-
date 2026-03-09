from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
options.page_load_strategy = 'normal'  
service = ChromeService()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("http://the-internet.herokuapp.com/login")
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")
    login_button = driver.find_element(By.CLASS_NAME, "radius")
    login_button.click()

    wait = WebDriverWait(driver, 10)
    flash_message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))

    text_from_flash = flash_message.text.strip()
    print(text_from_flash)

except Exception as e:
    print(f"Возникла ошибка: {e}")

finally:
    driver.quit()
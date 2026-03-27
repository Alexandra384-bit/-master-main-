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
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    third_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//img)[4]"))
    )

    WebDriverWait(driver, 10).until(
        lambda _: third_image.is_displayed() and int(third_image.get_attribute('naturalWidth')) > 0
    )
    
    third_image_src = third_image.get_attribute('src')
    print(third_image_src)
finally:
    driver.quit()
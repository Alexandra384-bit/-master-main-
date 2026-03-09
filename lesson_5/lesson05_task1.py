from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Упражнение 1. Клик по кнопке с CSS-классом
options = Options()
options.page_load_strategy = 'normal' 
driver = webdriver.Chrome(options=options)

try:
    
    driver.get("http://uitestingplayground.com/classattr")
    time.sleep(2)
    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    print("Кнопка нажата успешно!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
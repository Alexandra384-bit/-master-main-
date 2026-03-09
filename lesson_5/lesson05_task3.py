from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


options = Options()
options.page_load_strategy = 'normal'  
driver = webdriver.Chrome(options=options)

try:
    driver.get("http://the-internet.herokuapp.com/inputs")
    input_field = driver.find_element(By.TAG_NAME, 'input')
    input_field.send_keys('12345')
    input_field.clear()
    input_field.send_keys('54321')

    print("Задание выполнено успешно.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    driver.quit()
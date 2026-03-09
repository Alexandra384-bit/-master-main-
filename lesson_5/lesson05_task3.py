from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Настраиваем Chrome
options = Options()
options.page_load_strategy = 'normal'  # стратегия загрузки страницы
driver = webdriver.Chrome(options=options)

try:
    # Переходим на требуемый адрес
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Найдем поле ввода на странице
    input_field = driver.find_element(By.TAG_NAME, 'input')

    # Введем текст '12345'
    input_field.send_keys('12345')

    # Очистим поле ввода
    input_field.clear()

    # Введем новый текст '54321'
    input_field.send_keys('54321')

    print("Задание выполнено успешно.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закроем браузер
    driver.quit()
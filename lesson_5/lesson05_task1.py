from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Упражнение 1. Клик по кнопке с CSS-классом
options = Options()
options.page_load_strategy = 'normal'  # или 'eager', 'none'
driver = webdriver.Chrome(options=options)

try:
    # Переход на сайт
    driver.get("http://uitestingplayground.com/classattr")

    # Пауза для уверенности, что страница полностью загрузилась
    time.sleep(2)

    # Нажатие на кнопку
    button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

    print("Кнопка нажата успешно!")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Завершаем сессию и закрываем браузер
    driver.quit()
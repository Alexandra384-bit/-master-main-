from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Настройка браузера Chrome
options = Options()
options.page_load_strategy = 'normal'  # задаем стратегию загрузки страницы нормально

# Использование менеджера драйверов для автоматического выбора нужной версии драйвера
service = ChromeService()

# Открываем браузер Chrome
driver = webdriver.Chrome(service=service, options=options)

try:
    # Переход на целевую страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Вводим логин
    username_input = driver.find_element(By.ID, "username")
    username_input.send_keys("tomsmith")

    # Вводим пароль
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("SuperSecretPassword!")

    # Нажимаем кнопку входа
    login_button = driver.find_element(By.CLASS_NAME, "radius")
    login_button.click()

    # Ждем появление зеленого уведомления (flash success message)
    wait = WebDriverWait(driver, 10)
    flash_message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))

    # Получаем текст с зелёной плашки и выводим его в консоль
    text_from_flash = flash_message.text.strip()
    print(text_from_flash)

except Exception as e:
    print(f"Возникла ошибка: {e}")

finally:
    # Закрываем браузер
    driver.quit()
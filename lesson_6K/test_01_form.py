import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_form_validation():
    options = Options()
    options.page_load_strategy = 'normal'
    service = ChromeService()
    driver = webdriver.Chrome(service=service, options=options)
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Открыть страницу
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        driver.maximize_window()
        
        # --- Заполнение формы ---
        
        # First name
        first_name = wait.until(EC.visibility_of_element_located((By.NAME, "first-name")))
        first_name.send_keys("Иван")

        # Last name
        last_name = wait.until(EC.visibility_of_element_located((By.NAME, "last-name")))
        last_name.send_keys("Петров")

        # Address
        address = wait.until(EC.visibility_of_element_located((By.NAME, "address")))
        address.send_keys("Ленина, 55-3")

        # Email
        email = wait.until(EC.visibility_of_element_located((By.NAME, "e-mail")))
        email.send_keys("test@skypro.com")

        # Phone number
        phone = wait.until(EC.visibility_of_element_located((By.NAME, "phone")))
        phone.send_keys("+7985899998787")
        
        # Zip code (оставляем пустым)
        zip_code_field = wait.until(EC.visibility_of_element_located((By.NAME, "zip-code")))
        zip_code_field.clear()

        # City
        city = wait.until(EC.visibility_of_element_located((By.NAME, "city")))
        city.send_keys("Москва")
        
        # Country
        country = wait.until(EC.visibility_of_element_located((By.NAME, "country")))
        country.send_keys("Россия")

        # Job position
        job_position = wait.until(EC.visibility_of_element_located((By.NAME, "job-position")))
        job_position.send_keys("QA")

        # Company
        company = wait.until(EC.visibility_of_element_located((By.NAME, "company")))
        company.send_keys("SkyPro")
        
        # 2. Нажать кнопку Submit, НО предотвратить переход
        submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        
        # Вариант 1: Нажать через JavaScript, чтобы форма не отправилась
        driver.execute_script("arguments[0].click();", submit_button)
        print("Кнопка Submit нажата (через JavaScript)")
        
        # Даем время на выполнение JavaScript валидации
        time.sleep(1)
        
        # 3. Проверяем поле zip-code на наличие класса is-invalid
        zip_code_input = driver.find_element(By.NAME, "zip-code")
        zip_code_class = zip_code_input.get_attribute("class")
        print(f"Zip code class after validation: '{zip_code_class}'")
        
        # Проверяем, что класс is-invalid присутствует
        assert "is-invalid" in zip_code_class, \
            f"Поле Zip code не подсвечено красным цветом. Класс: {zip_code_class}"
        
        # 4. Проверяем, что все остальные поля имеют класс is-valid
        valid_fields = [
            "first-name", "last-name", "address", "e-mail", 
            "phone", "city", "country", "job-position", "company"
        ]
        
        print("\nПроверка остальных полей:")
        all_valid = True
        for field_name in valid_fields:
            field = driver.find_element(By.NAME, field_name)
            field_class = field.get_attribute("class")
            print(f"{field_name}: class = '{field_class}'")
            
            if "is-valid" not in field_class:
                all_valid = False
                print(f"  ⚠️ Поле {field_name} НЕ имеет класс is-valid")
        
        assert all_valid, "Не все поля имеют класс is-valid"
        
        print("\n✅ Тест успешно пройден: валидация формы работает корректно!")
        print("   - Поле Zip code подсвечено красным (is-invalid)")
        print("   - Все остальные поля подсвечены зеленым (is-valid)")
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        driver.save_screenshot("error_screenshot.png")
        print(f"Текущий URL: {driver.current_url}")
        raise
        
    finally:
        driver.quit()
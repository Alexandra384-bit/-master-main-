from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def main():
    # Настройки браузера
    options = Options()
    options.page_load_strategy = 'normal'  # Нормальная стратегия загрузки страницы

    # Установка Chrome Driver
    service = Service(ChromeDriverManager().install())

    # Создание экземпляра браузера Chrome
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Переход на целевую страницу
        driver.get("http://uitestingplayground.com/dynamicid")

        # Клик по синему элементу с классом btn-primary
        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
        button.click()

        print("Кнопка нажата успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


    finally:
        # Закрытие браузера после выполнения
        driver.quit()

if __name__ == "__main__":
    main()
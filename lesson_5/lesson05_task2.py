from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def main():
    options = Options()
    options.page_load_strategy = 'normal' 
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("http://uitestingplayground.com/dynamicid")
        button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
        button.click()

        print("Кнопка нажата успешно!")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


    finally:
        driver.quit()

if __name__ == "__main__":
    main()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Настройка ChromeOptions для подключения MetaMask
chrome_options = Options()
chrome_options.add_argument("--start-maximized")

# Путь к вашему chromedriver
PATH = "/path/to/chromedriver"

# Запуск браузера
driver = webdriver.Chrome(service=Service(PATH), options=chrome_options)

# Открытие сайта
driver.get("https://www.dusted.app/ ")
print("Открыт сайт Dust'd")

# Ждём загрузки страницы
time.sleep(5)

try:
    # Нажимаем кнопку "Enter App" (предположительно это кнопка входа)
    enter_button = driver.find_element(By.XPATH, '//button[contains(text(), "Enter App")]')
    enter_button.click()
    print("Кнопка 'Enter App' нажата")
    time.sleep(3)

    # Здесь должна появиться кнопка подключения кошелька
    connect_wallet_button = driver.find_element(By.XPATH, '//button[contains(text(), "Connect Wallet")]')
    connect_wallet_button.click()
    print("Кнопка 'Connect Wallet' нажата")
    time.sleep(3)

    # Переключаемся на окно MetaMask (не реализуется здесь, так как это отдельное окно ОС)
    print("Подтвердите подключение кошелька в MetaMask вручную.")

except Exception as e:
    print("Ошибка при автоматизации:", e)

finally:
    # Можно оставить браузер открытым для ручного завершения входа
    input("Нажмите Enter, чтобы закрыть браузер...")
    driver.quit()

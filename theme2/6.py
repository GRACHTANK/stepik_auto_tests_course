from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter first name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter last name"]')
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter email"]')
    input3.send_keys("test@mail.ru")
    button = browser.find_element(By.ID, 'file')
    button.send_keys(r'C:\Users\yara\PycharmProjects\pythonProject\venv\auto_test\file.txt')
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


link = "https://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)
    num1 = browser.find_element(By.ID, 'num1')
    num1 = num1.text
    num2 = browser.find_element(By.ID, 'num2')
    num2 = num2.text
    print(num1, num2)
    sum = int(num1) + int(num2)
    sum = str(sum)
    #chislo = browser.find_element(By.ID, 'dropdown').click()
    #chislo1 = browser.find_element(By.CSS_SELECTOR, (f"[value='{sum}']"))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)
    #chislo1.click()
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-default')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    x = browser.find_element(By.ID, 'input_value')
    x = x.text
    y = calc(x)
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

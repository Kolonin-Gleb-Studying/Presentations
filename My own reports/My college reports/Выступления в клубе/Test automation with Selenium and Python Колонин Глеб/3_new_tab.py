# webdriver = набор команд для управления браузером
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://130.193.37.179/app/pets")

    # Попали на основную страницу
    time.sleep(3)

    # Тест кнопки о нас
    button = browser.find_element(By.CSS_SELECTOR, "form > a:nth-child(1)")
    button.click()

    # Проверка содержимого страницы на наличие нужных данных

    about_us = browser.find_element(By.CSS_SELECTOR, "h2")
    about_us = about_us.text

    assert about_us == "О нас", "Тест страницы 'о нас' - не пройден!" # Сообщение при ошибке.

    time.sleep(3)

finally:
    time.sleep(5)
    browser.quit()

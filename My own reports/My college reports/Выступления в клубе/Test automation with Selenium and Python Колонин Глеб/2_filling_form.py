from selenium import webdriver

# Для ещё 1 способа написания Селекторов --> browser.find_element(By.CSS_SELECTOR, "#input_value")
# from selenium.webdriver.common.by import By

import time # Для визуальных задержек

# Для того, чтобы браузер закрывался в любом случае и не происходила утечка 
# ресурсов компьютера нужно размещать тесты в try/finaly
try: 
  link = "https://suninjuly.github.io/simple_form_find_task.html"
  browser = webdriver.Chrome()
  browser.get(link)

  # Заполнение формы с помощью css селекторов
  input1 = browser.find_element_by_tag_name("input")
  input1.send_keys("Ivan")
  input2 = browser.find_element_by_name("last_name")
  input2.send_keys("Petrov")
  input3 = browser.find_element_by_class_name("city")
  input3.send_keys("Smolensk")
  input4 = browser.find_element_by_id("country")
  input4.send_keys("Russia")

  # Отправка заполненной формы
  button = browser.find_element_by_css_selector("#submit_button")
  button.click()

finally:
  # ожидание чтобы визуально оценить результаты прохождения скрипта
  # Копируем код прохождения
  time.sleep(10)
  # закрываем браузер после всех манипуляций
  browser.quit()


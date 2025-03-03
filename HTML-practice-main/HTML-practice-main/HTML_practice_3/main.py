from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('http://localhost:8080')

    ol = driver.find_element(By.TAG_NAME,'oi')
    li_list = ol.find_elements(By.TAG_NAME,'li')
    
    for li in li_list:
        print(li.text)
    
    big_list = driver.find_elements(By.TAG_NAME,'big')
    for big in big_list:
        print(big.text)

    ui = driver.find_element(By.TAG_NAME,'ui')
    body = ui.find_elements(By.TAG_NAME,'body')
    print(body.text)
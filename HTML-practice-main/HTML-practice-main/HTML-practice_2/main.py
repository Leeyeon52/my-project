from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:
    driver.get('http://localhost:8080')
    
    title = driver.find_element(By.TAG_NAME,'title')
    print(title.text)

    img_list = driver.find_elements(By.TAG_NAME,'img')
    for img in img_list:
        print(img.get_attribute('src'))

    div_list = driver.find_elements(By.TAG_NAME,'div')
    for div in div_list:
        p_list = div.find_elements(By.TAG_NAME,'p')
        for p in p_list:
            print(p.text)

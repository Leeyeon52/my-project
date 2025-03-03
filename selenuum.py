from selenium import webdriver
from selenium.webdriver.common.by import By

with webdriver.Chrome() as driver:  # 실행브라우저
    driver.get('https://news.naver.com')
...
driver.quit()


e = driver.find_element(By.TAG_NAME,'body')
print(e.text)

for e in e_list:
    print(e.text)

e_list = driver.find_elements(By.TAG_NAME,'p')
e =  e_list[1]



e_list = driver.find_elements(By.TAG_NAME,'div').find_element(By.TAG_NAME,'p')
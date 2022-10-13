from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import pandas as pd

driver = webdriver.Chrome(executable_path='D:/webdrivers/chromedriver.exe')
driver.get('https://www.jobsite.co.uk/')
driver.maximize_window()
time.sleep(1)

cookie = driver.find_element(By.XPATH, '//*[@id="ccmgt_explicit_accept"]')
try:
    cookie.click()
except:
    pass

job_title = driver.find_element(By.ID, 'keywords')
job_title.click()
job_title.send_keys('Data Engineering')
time.sleep(1)

location = driver.find_element(By.ID, 'location')
location.click()
location.send_keys('Manchester')
time.sleep(1)

dropdown = driver.find_element(By.ID, 'Radius')
radius = Select(dropdown)
radius.select_by_visible_text('30 miles')
time.sleep(1)

search = driver.find_element(By.XPATH, '//*[@id="search-button"]')
search.click()
time.sleep(20)

data1 = []
for k in range(3):
    titles = driver.find_elements(By.XPATH, '//div[@class="sc-fzooss kBgtGS"]/a/h2')
    company = driver.find_elements(By.XPATH, '//div[@class="sc-fzoiQi kuzZTz"]')
    location = driver.find_elements(By.XPATH, '//ul[@class="sc-fznLxA bAwAgE"]/li[1]')
    salary = driver.find_elements(By.XPATH, '//dl[@class="sc-fzoJMP jpodhy"]')
    posted = driver.find_elements(By.XPATH, '//ul[@class="sc-fznLxA bAwAgE"]/li[2]')
    description = driver.find_elements(By.XPATH, '//div[@class="sc-fzoYkl kSkZOQ"]/a/span')

    for i in range(len(titles)):
        data = {'Job_title': titles[i].text, 'Company': company[i].text, 'Location': location[i].text, 'Salary': salary[i].text, 'Posted': posted[i].text, 'Job_description': description[i].text}
        data1.append(data)

    next = driver.find_element(By.XPATH, '//a[@aria-label="Next"]')
    next.click()
    time.sleep(20)

df = pd.DataFrame(data=data1)
df.to_csv('job_scraping_pagination.csv', index=False)
driver.close()

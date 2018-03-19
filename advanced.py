from selenium import webdriver
import time

# Opening Chrome in incognito mode
option = webdriver.ChromeOptions()
option.add_argument('--start-maximized')

driver = webdriver.Chrome(chrome_options=option)

driver.get('https://www.glassdoor.com/index.htm')

driver.find_element_by_css_selector('#KeywordSearch').send_keys('Data Science')

driver.find_element_by_css_selector('#LocationSearch').clear()
driver.find_element_by_css_selector('#LocationSearch').send_keys('Hong Kong')

driver.find_element_by_css_selector('#HeroSearchButton').click()

jobs_list = driver.find_elements_by_xpath('//ul[@class="jlGrid hover"]/li')

# Write it in a text files

jobs_outfile = open('jobs.txt', 'w')

for job in jobs_list:
    jobs_outfile.write(job.text)

jobs_outfile.close()


time.sleep(5)
driver.close()
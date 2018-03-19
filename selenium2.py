from selenium import webdriver
import pandas as pd

# With page pagination

# Open up Firefox to Navigate to the page
driver = webdriver.Firefox()

driver.get('http://econpy.pythonanywhere.com/ex/001.html')

# number of pages - 1
num_pages = len(driver.find_elements_by_css_selector('font'))

# initialize lists
a = []
b = []

for i in range(num_pages):
    url = 'http://econpy.pythonanywhere.com/ex/' + '00' + str(i+1) + '.html'
    driver.get(url)
    buyers = driver.find_elements_by_css_selector('div div')
    prices = driver.find_elements_by_css_selector('.item-price')
    buyers = [buyers[i].text for i in range(len(buyers))]
    prices = [float(prices[i].text.strip('$')) for i in range(len(buyers))]
    a.extend(buyers)
    b.extend(prices)

# Put it into a DataFrame
df = pd.DataFrame({'Buyers': a, 'Prices': b})

print(df)

df.to_csv('result.csv', index=False)

# Close Browser
driver.close()

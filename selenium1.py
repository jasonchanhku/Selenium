from selenium import webdriver
import pandas as pd
# Open up Firefox to Navigate to the page
driver = webdriver.Firefox()

driver.get('http://econpy.pythonanywhere.com/ex/001.html')

buyers = driver.find_elements_by_css_selector('div div')

prices = driver.find_elements_by_css_selector('.item-price')

num = len(buyers)

buyers = [buyers[i].text for i in range(num)]
prices = [float(prices[i].text.strip('$')) for i in range(num)]

# Put it into a DataFrame
df = pd.DataFrame({'Buyers': buyers, 'Prices': prices})

print(df)
# Close Browser
driver.close()

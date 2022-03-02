import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromewd/chromedriver.exe')
driver.get('https://oxylabs.io/blog')
results = []
content = driver.page_source
soup = BeautifulSoup(content)

driver.quit()
for element in soup.findAll(attrs='blog-cart__content-wrapper'):
    name = element.find('h2')
    if name not in results:
        results.append(name.text)
df = pd.DataFrame({'Names:results'})
df.to_csv('names.csv', index=False, encoding='utf-8')
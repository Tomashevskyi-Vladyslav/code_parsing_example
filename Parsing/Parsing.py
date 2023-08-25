from bs4 import BeautifulSoup
from selenium import webdriver
import time

url = r'https://www.re-store.ru/catalog/MYD82RU-A/'

def get_html_new(url):
    with webdriver.Chrome() as browser:
        browser.get(url)
        time.sleep(2)
        html = browser.page_source
    return html

html = get_html_new(url)
soup = BeautifulSoup(html, 'html.parser')
tag = soup.find("body")
print(tag)

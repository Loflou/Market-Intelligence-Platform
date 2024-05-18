from selenium import webdriver
from selenium.webdriver.chrome service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import json
import time

def setup_driver():
    options = Options()
    options.headless = True
    service = Service('/path/to/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def scrape_website(url):
    driver = setup_driver()
    driver.get(url)
    time.sleep(3) # Adjust sleep time as necessary for the page to load
    elements = driver.find_elements(By.TAGNAME, 'example_tag')
    data = [element.text for element in elements]
    driver.quit()
    return data

def main():
    with open('config/urls.json') as f:
        urls = json.load(f)
    all_data = {}
    for category, url_list in urls.items():
        category_data = []
        for url in url_list:
            data = scrape_website(url)
            category_data.append({url: data})
        all_data[category] = category_data

    with open('data/scraped_data.json', 'w') as f:
        json.dump(all_data, f, indent=4)

if __name__ == '__main__':
    main()

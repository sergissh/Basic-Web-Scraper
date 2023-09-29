import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
def scrap(urls, dataframe):
    for url in urls:
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        browser = webdriver.Chrome(
            options = options 
        )
        browser.get(url)
        try:
            myElem = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button#onetrust-accept-btn-handler')))
            try:
                price = browser.find_element(By.CSS_SELECTOR, ".text-h4.font-weight-bold").text
                author = browser.find_element(By.CLASS_NAME, "text--darken-1").text
                title = browser.find_element(By.CSS_SELECTOR, "h1").text
                print({"Title": title, "Author": author, "Price": price})
                dataframe.loc[len(dataframe)] = [title, author, price]                
                browser.quit()
            except selenium.common.exceptions.NoSuchElementException:
                browser.quit()
                continue
        except selenium.common.exceptions.NoSuchWindowException:
            browser.quit()
            continue

    return dataframe
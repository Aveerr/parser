from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = webdriver.FirefoxOptions()
#options.set_preference('dom.webdriver.enabled', False)
options.add_argument('user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0')
driver = webdriver.Firefox(options=options)

url = 'https://ozon.by/'
electronics_xpath = '/html/body/div[1]/div/div[1]/header/div[2]/div/div/ul/li[3]/a'
electronics_category_xpath = [
    '/html/body/div[1]/div/div[1]/div[2]/div[3]/div',
    '/html/body/div[1]/div/div[1]/div[2]/div[4]/div'
]

try:
    #driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"
    
    driver.get(url)
    huh = driver.get(driver.find_element(By.XPATH, electronics_xpath).get_attribute('href'))
    first_category_block = driver.find_element(By.XPATH, electronics_category_xpath[0])
    fcb_all_item = first_category_block.find_element(By.TAG_NAME, 'div')
    print(first_category_block)
    
    time.sleep(5)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
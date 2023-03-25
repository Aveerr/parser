from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

try:
    # driver.get("https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html")
    driver.get("https://ozon.by/")

    link_redirect = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/header/div[2]/div/div/ul/li[3]/a").get_attribute('href')
    driver.get(link_redirect)

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[4]/div/div[2]").click() #button_audio
    link_redirect = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/aside/section/main/div[2]/div[2]/div[1]/div/a").get_attribute('href')
    driver.get(link_redirect)

    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/aside/div[3]/div[2]/div/span[1]/label/div[2]/div/span").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/aside/div[4]/div[2]/span/span").click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div/aside/div[4]/div[2]/div[1]/div[1]/div/input"))).send_keys("xiaomi")
    driver.find_element(By.CSS_SELECTOR,"#layoutPage > div.b0 > div.container.b4 > div:nth-child(2) > div:nth-child(1) > div > aside > div:nth-child(5) > div:nth-child(2) > div.aa9f > div > a:nth-child(1) > label > div.x7-a4").click()

    time.sleep(100)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

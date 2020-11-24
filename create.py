import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 

options = Options()
options.add_argument("--headless")

PATH = '<driver-path>/chromedriver'
driver =webdriver.Chrome(chrome_options=options,executable_path=PATH)
path = '<project-path>'

def create ():
    foldername = str(sys.argv[1])
    os.makedirs(path + foldername)
    driver.get('https://github.com/login')
    print("@ ",driver.title)
    username = driver.find_element_by_xpath('//*[@id="login_field"]')
    username.send_keys("<github-username>")
    password = driver.find_element_by_xpath('//*[@id="password"]')
    password.send_keys("<github-password>",Keys.RETURN)
    print("@ ",driver.title)

    profile = driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
    profile.send_keys(Keys.RETURN)
    print("@ ",driver.title)

    repo = driver.find_element_by_id('repository_name')
    repo.send_keys(foldername)
    create = driver.find_element_by_css_selector('button.first-in-line')
    create.submit()
    print("@ ",driver.title)

if __name__=="__main__":
    create()
    driver.quit()

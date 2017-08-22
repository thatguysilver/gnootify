from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import sys, requests
import time

def page_iter():
    'cycles through the gnoosic.com pages'
    temp_list = []
    driver = webdriver.Firefox()
    driver.get('http://gnoosic.com/faves.php')

    if len(sys.argv) > 1:
        i = 1
        #fave = ''
        for item in sys.argv[1:]:
            fave = driver.find_element_by_name(f'Fave0{i}')
            fave.send_keys(item)
            i += 1
        fave.send_keys(Keys.RETURN)

    idk_list = []
    for i in range(11):
        time.sleep(10)
        try:
            driver.find_element_by_name('Rate00').click()
        except NoSuchElementException:
            print('We\'re done here!')
    print('loop exited')
    driver.find_element_by_xpath('//tr[3]/td/form/table/tbody/tr[4]/td/input').click()

    for i in range(11):
        text = driver.find_element_by_xpath(f'//tr[3]/td/div[2]/div[2]/a[{i+1}]').text

        print(text)

if __name__ == '__main__':
    page_iter()

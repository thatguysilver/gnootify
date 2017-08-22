from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#from bs4 import BeautifulSoup as bs
import sys
import time

def gnoot_iter():
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
    for i in range(10):
        time.sleep(10)
        try:
            driver.find_element_by_name('Rate00').click()
        except NoSuchElementException:
            print('We\'re done here!')
    print('loop exited')
    driver.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/form/table/tbody/tr[4]/td/input')

if __name__ == '__main__':
    gnoot_iter()

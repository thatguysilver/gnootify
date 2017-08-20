from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time

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

time.sleep(30)
try:
    driver.find_element_by_name('Rate00').click()
except TypeError:
    print('We\'re done here!')

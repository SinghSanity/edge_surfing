import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from search_list import get_search_list

options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

search_list = get_search_list()

def run():
    '''Main function. Gets Edge webdriver, goes to bing.com and then searches for every item in the list.'''
    driver = webdriver.Edge(options=options)
    driver.get('https://bing.com')
    time.sleep(10)
    for i in search_list:
        element = driver.find_element(By.ID, 'sb_form_q')
        element.clear()
        element.send_keys(i)
        time.sleep(10)
    driver.quit()

if __name__ == '__main__':
    run()
import time
def incognito():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')
    search=driver.find_element_by_id('lst-ib')
    incognito=search.send_keys(Keys.CONTROL+Keys.SHIFT+'N')
    driver.switch_to_window(driver.window_handles[-1])
    driver.get('https://web.whatsapp.com/')
    time.sleep(5)
incognito()
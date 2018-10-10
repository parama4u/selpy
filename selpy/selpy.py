import selenium.webdriver
from selenium.webdriver.common.by import By

class SelPy:

    driver=None
    def __init__(self):
        try:
            dr=selenium.webdriver.Chrome("driver/chromedriver.exe")
            self.driver=dr
        except:
            print("Error while starting chrome driver")
    def navigate(self,url):
        self.driver.delete_all_cookies()
        self.driver.get(url)
        self.driver.find_element(By.XPATH, '//button[text()="OK"]').click()
        
        
    def curURL(self):
        return self.driver.current_url

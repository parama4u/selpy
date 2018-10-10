import selenium.webdriver

class SelPy:


    driver=None

    def __init__(self):
        try:
            dr=selenium.webdriver.Chrome()
            dr.get(url)
            self.driver=dr

        except:
            print("Error while starting chrome driver")

    def navigate(self,url):
        self.driver.get(url)

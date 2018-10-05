import selenium.webdriver

class SelPy:


    driver=None

    def __init__(self):
        pass

    def start_chrome(self,url):
        try:
            dr=selenium.webdriver.Chrome()
            dr.get(url)
            self.driver=dr
        except:
            print("Error while starting chrome driver")


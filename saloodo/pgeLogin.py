
import selpy.selpy
from selenium.webdriver.common.by import By

class PageLogin:

    obj =  None


    def __init__(self):
        self.obj=selpy.selpy.SelPy()

    def fldEmail(self):
        return self.obj.find_element(By.NAME,'_email')

    def fldPassWord(self):
        retrun self.obj.find_element(By.NAME,'_password')

    def btnLogin(self):
        return self.obj.find_element(By.XPATH, '//button[text()="Log in"]')

    def setEmail(self,txtEmail):
        self.fldEmail.typeText(txtEmail)

    def setPassWord(self,txtPassWord):
        self.fldPassword.typeText(txtPassWord)


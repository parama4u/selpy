
import selpy.selpy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class PageLogin:

    obj =  None


    def __init__(self):
        self.obj=selpy.selpy.SelPy()
    
    def navigate(self,url):
        self.obj.navigate(url)

    def fldEmail(self):
        try:
            return self.obj.driver.find_element(By.NAME,'_email')
        except NoSuchElementException:
            return False

    def fldPassWord(self):
        try:
            return self.obj.driver.find_element(By.NAME,'_password')
        except NoSuchElementException:
            return False


    def btnLogin(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//button[text()="Log in"]')
        except NoSuchElementException:
            return False
        
    def btnRegister(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//button[text()="Register"]')
        except NoSuchElementException:
            return False


    def lnkResetPass(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//contains[text()="Reset Password"]')
        except NoSuchElementException:
            return False
        
        
        
    def lnkRememberMe(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//contains[text()="Keep me logged in on this computer"]')
        except NoSuchElementException:
            return False
        
    def lnkLanguages(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//contains[text()="English"]')
        except NoSuchElementException:
            return False

    
    def lnkSupport(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//contains[text()="Support"]')
        except NoSuchElementException:
            return False
    
        
    def setEmail(self,txtEmail):
        self.fldEmail.typeText(txtEmail)

    def setPassWord(self,txtPassWord):
        self.fldPassword.typeText(txtPassWord)



import selpy.selpy
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

class PageLogin:

    obj =  None


    def __init__(self):
        self.obj=selpy.selpy.SelPy()
    
    def navigate(self):
        self.obj.navigate("https://demo.saloodo.com/login")

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
            return self.obj.driver.find_element(By.XPATH, '//button[text()="Log In "]')
        except NoSuchElementException:
            return False
        
    def btnRegister(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//button[text()="Register"]')
        except NoSuchElementException:
            return False


    def lnkResetPass(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//div[text()="Reset password "]')
        except NoSuchElementException:
            return False
        
        
        
    def lnkRememberMe(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//label[text()="Keep me logged in on this computer"]')
        except NoSuchElementException:
            return False
        
    def lnkLanguages(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//a[text()="English"]')
        except NoSuchElementException:
            return False

    
    def lnkSupport(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//span[text()="Support"]')
        except NoSuchElementException:
            return False
    
    
    def lnkPrvc(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//a[text()="Privacy Notice"]')
        except NoSuchElementException:
            return False
        
    def lnkTC(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//a[text()="Saloodo\'s Terms & Conditions"]')
        except NoSuchElementException:
            return False
        
    def lnkLegl(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//a[text()="Legal Notice"]')
        except NoSuchElementException:
            return False
        
    def lnkPress(self):
        try:
            return self.obj.driver.find_element(By.XPATH, '//a[text()="Press"]')
        except NoSuchElementException:
            return False
        
    
        
    def setEmail(self,txtEmail):
        self.fldEmail().send_keys(txtEmail)

    def setPassWord(self,txtPassWord):
        self.fldPassWord().send_keys(txtPassWord)


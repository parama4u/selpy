
import selpy.selpy

class PageLogin:

    obj =  None


    def __init__(self):
        self.obj=selpy.selpy.SelPy()
        print("PageLogin")
        self.obj.start_chrome("http://www.google.co.in")





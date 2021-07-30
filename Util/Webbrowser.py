from selenium import webdriver

Browser = "Chrome"


class WebBrowser:
    def __init__(self):
        self.driver = None

    def getdriver(self):
        if Browser == "Chrome":
            self.driver = webdriver.Chrome("D:\\Automation\\10 Perals Project\\Drivers\\chromedriver.exe")

        elif Browser == "Firefox":
            webdriver.Chrome("D:\\Automation\\10 Perals Project\\Drivers\\chromedriver.exe")

        self.driver.maximize_window()
        self.driver.get("https://www.google.com/")
        return self.driver



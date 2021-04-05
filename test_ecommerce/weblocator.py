from abc import ABC


class WebLocators(ABC):
    def __init__(self, webdriver, url):
        self.webdriver = webdriver
        self.url = url

    def open(self):
        self.webdriver.get(self.url)

    def find_element(self, locator):
        self.webdriver.find_element(*locator)
        
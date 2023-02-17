from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Utils:
    def __init__(self, driver):
        self.driver = driver

    def find_xpath_element(self, path):
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((
            By.XPATH, path)))
    
        return self.driver.find_element('xpath', path)

class Constants:
    twitterHomeUrl = 'https://twitter.com/home'
    twitterLoginUrl = 'https://twitter.com/i/flow/login'
    emailInputXpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input'
    usernameInputXpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input'
    passInputXpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'
    searchButtonXpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]/div'
    searchBoxXpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[1]/div[2]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input'
    peopleTabXpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/div'
    firstPersonXpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div/div/div/div[2]/div[2]/div[1]/div[1]/div'
    postingsClass = 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0'

class BreakIt(Exception):
    pass
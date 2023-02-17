from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from common import Utils, Constants, BreakIt
import sys
import argparse
from bs4 import BeautifulSoup
import time
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import os

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help = "username of the twitter account")
parser.add_argument("-e", "--email", help = "email id of the twitter account")
parser.add_argument("-p", "--password", help = "password of the twitter account")
parser.add_argument("-per", "--person", help = "person name, go with a proper account name for accurate results")
parser.add_argument('-n' , "--noOfTweets", default = 100, type = int, help = "no of tweets you want to extract")
args = parser.parse_args()

#initialize the driver
driver = webdriver.Chrome(ChromeDriverManager().install())
utils = Utils(driver)

#open twitter
driver.get(Constants.twitterLoginUrl)

#find the email box and enter email
emailBox = utils.find_xpath_element(Constants.emailInputXpath)
emailBox.send_keys(args.email)
emailBox.send_keys(Keys.ENTER)

#incase twitter asks for username because of unusual activity
try:
    usernameBox = utils.find_xpath_element(Constants.usernameInputXpath)
    usernameBox.send_keys(args.username)
    usernameBox.send_keys(Keys.ENTER)    
except:
    print('no unusual activity detected by twitter yet, lucky')

#enter the password
passBox = utils.find_xpath_element(Constants.passInputXpath)
passBox.send_keys(args.password)
passBox.send_keys(Keys.ENTER)

#find the search button
utils.find_xpath_element(Constants.searchButtonXpath).click()

#enter celebrity name in searchbox
searchBox = utils.find_xpath_element(Constants.searchBoxXpath)
searchBox.send_keys(args.person)
searchBox.send_keys(Keys.ENTER)

#go to people tab
utils.find_xpath_element(Constants.peopleTabXpath).click()

#choosing the first on the people list
utils.find_xpath_element(Constants.firstPersonXpath).click()

#extract tweets for the user
data = set()
old_height = 0

while True:
    if(len(data) == args.noOfTweets):
        break
    
    soup = BeautifulSoup(driver.page_source, 'lxml')
    postings = soup.find_all('div', 'div', class_ = Constants.postingsClass)
    
    for posting in postings:
        data.add(posting.text)
        if(len(data) == args.noOfTweets):
            break
    
    #get the height of the current page
    new_height = driver.execute_script('return document.body.scrollHeight')
    
    #if reached the last post
    if(new_height == old_height):
        break
        
    old_height = new_height
    
    #scroll further
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(1)

#store it in a csv
if not os.path.exists('./tweets'):
    os.mkdir('./tweets')
    
pd.DataFrame(list(data), columns = ['tweet']).to_csv(f'./tweets/{args.person}_tweets.csv')
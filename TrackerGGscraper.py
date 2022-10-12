# -*- coding: utf-8 -*-
"""
Tracker.gg WebScraper

Created on Fri Oct  7 11:31:32 2022

@author: Brian
"""

from selenium import webdriver 
from selenium.webdriver.common.by import By
import pandas as pd




Driver_path = r'C:\Users\Brian\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(executable_path = Driver_path)


def get_data(): 
    
    data = driver.find_elements(By.CLASS_NAME, ('st-content__item') )
    values = []

    for element in data:
        values.extend(element.text.strip().split('\n'))
    return values


def get_headers():
    headers = driver.find_elements(By.CLASS_NAME, ('st-header') )
    variables = []
    for element in headers:
        variables.extend(element.text.strip().split('\n'))
    
        
    variables.insert(1, "Type")
    return variables
        
def make_df():
    n = len(get_headers())

    x = [get_data()[i:i + n] for i in range(0, len(get_data()), n)]

    df = pd.DataFrame(x, columns = get_headers())
    print(df)


def program(targeturl):
    driver.get(targeturl)
    
    make_df()
    
    
if __name__ == "__main__":
    print("This is a webscraper that fetches data from Tracker.gg. Paste the URL of the desired profile in the 'Agent' tab, and the program will output a Dataframe of the Agents tab")    
    webPage = input("Paste URL here:")

    keyword = "agents"
    if keyword in webPage: 
        program(webPage)



driver.quit()
    

from selenium import webdriver  
import time
import random
#import multiprocessing,os
import os

# chromedriver = "C:\Program Files\geckodriver.exe"
# os.environ["webdriver.Firefox.driver"] = chromedriver

start_interval=5
end_interval=10

url='http://www.baidu.com'

def open_web():
	driver=webdriver.Firefox()
	driver.get(url)

	time.sleep(random.randint(start_interval,end_interval))

	driver.quit()

open_web()

		

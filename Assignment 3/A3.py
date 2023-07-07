# Importing required libraries

# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the Apple.com homepage
driver.get("https://www.apple.com/")
time.sleep(3)

# Finding the iPhone menu button and hover on it
iphone_button = driver.find_element(By.XPATH, "/html/body/div[1]/nav/div/ul/li[2]/div/div/div[4]")
iphone_button.click()
time.sleep(3)

# Finding the learn more button and scroll to it
learn_more_button = driver.find_element(By.XPATH, "/html/body/main/section[3]/div/div/div[1]/div[3]/div/p/a/span[1]")
action = ActionChains(driver)
action.scroll_to_element(learn_more_button).perform()
time.sleep(3)

# Finding the iPhone14Pro image and click
iphone_14pro_image = driver.find_element(By.XPATH, "/html/body/main/section[3]/div/div/div[1]/div[1]/div/a/figure")
iphone_14pro_image.click()
time.sleep(6)

# Verifying that the iPhone 14 Pro page has loaded
assert "iPhone 14 Pro and iPhone 14 Pro Max - Apple" in driver.title

# Finding the gold colour button and click
gold_colour_button = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/form/fieldset/ul/li[2]")
gold_colour_button.click()
time.sleep(3)

# Finding the white colour button and click
white_colour_button = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/form/fieldset/ul/li[3]")
white_colour_button.click()
time.sleep(3)

# Finding the black colour button and click
black_colour_button = driver.find_element(By.XPATH, "/html/body/main/div[2]/div/form/fieldset/ul/li[4]")
black_colour_button.click()
time.sleep(3)

# Closing the webdriver
driver.close()

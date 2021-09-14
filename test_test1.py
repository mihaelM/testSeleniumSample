import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

class TestTest1():
  def setup_method(self, method):
    self.driver = webdriver.Chrome() #self.driver = webdriver.Chrome("/home/mihael/Desktop/selenium/chromedriver_linux64/chromedriver")
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test1(self):
    self.driver.get("https://www.google.hr")
    time.sleep(1)
    self.driver.find_element(By.ID, "L2AGLb").click()
    time.sleep(1)
    self.driver.find_element(By.NAME, 'q').send_keys('kokos')
    time.sleep(1)
    self.driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)

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

class TestTest3():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_test3(self):
    self.driver.get("https://www.netokracija.com/")
    time.sleep(1)
    self.driver.set_window_size(1388, 528)
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Poslovi").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Kalendar").click()
    time.sleep(1)
    self.driver.find_element(By.LINK_TEXT, "Podcast").click()
  

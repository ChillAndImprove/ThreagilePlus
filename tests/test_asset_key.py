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
from selenium.webdriver.support import expected_conditions as EC  # Added alias
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

class TestOpenGraph():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")  # Or just "--headless"
    options.add_argument("--window-size=1854,1011")


    self.driver = webdriver.Chrome(options)
    self.vars = {}

  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_asset_key(self):
    def relative_click(orig_x, orig_y, ref_width, ref_height, width, height):
        """Helper to calculate position and perform relative click"""
        rel_x = orig_x / ref_width
        rel_y = orig_y / ref_height
        x = int(width * rel_x)
        y = int(height * rel_y)
        actions = ActionChains(self.driver)
        actions.move_by_offset(x, y).click().perform()
        actions.move_by_offset(-x, -y).perform()

    # Initial setup
    self.driver.get("http://0.0.0.0:8000/indexTest.html")
    #window_size = self.driver.get_window_size()
    #width, height = window_size['width'], window_size['height']
    self.driver.set_window_size(1854, 1011)
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .geBtn").click()
    self.driver.switch_to.default_content()
    wait = WebDriverWait(self.driver, 10)

    # Get current window size
    window_size = self.driver.get_window_size()
    width, height = window_size['width'], window_size['height']

    # Reference resolution
    ref_width, ref_height = 1854, 1011

    # Step 1: Click Asset
    relative_click(1215, 103, ref_width, ref_height, width, height)

    # Step 2: Click on second position
    relative_click(1746, 156, ref_width, ref_height, width, height)

    self.driver.switch_to.active_element.send_keys(Keys.CONTROL, 'a')
    self.driver.switch_to.active_element.send_keys("foo")
    relative_click(1097, 506, ref_width, ref_height, width, height)

    # === Check if one technical asset exists ===
    threagile_data = self.driver.execute_script("return editorUi.editor.graph.model.threagile.toJSON();")
    technical_assets = threagile_data.get("technical_assets", {})

    assert isinstance(technical_assets, dict), "technical_assets is not a dictionary"
    assert len(technical_assets) >= 1, "No technical assets were found after click"

    # === Check for specific technical asset key ===
    assert "foo" in technical_assets, "Expected technical asset key 'foo' not found"


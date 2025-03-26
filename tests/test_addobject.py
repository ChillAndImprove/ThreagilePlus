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

class TestOpenGraph():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_addobject(self):
    self.driver.get("http://127.0.0.1:8000/indexTest.html")
    self.driver.set_window_size(912, 1011)
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.ID, "cancelButton").click()
    wait = WebDriverWait(self.driver, 10)
    # Get current window size
    window_size = self.driver.get_window_size()
    width = window_size['width']
    height = window_size['height']

    # Reference resolution and coordinates
    ref_width = 1854
    ref_height = 1011
    orig_x = 28
    orig_y = 127

    # Convert to relative
    rel_x = orig_x / ref_width
    rel_y = orig_y / ref_height

    # Scale to current screen size
    x = int(width * rel_x)
    y = int(height * rel_y)


    # Move and click at (x, y)
    actions = ActionChains(self.driver)
    actions.move_by_offset(x, y).click().perform()

    # Reset the mouse position (important if you want to click again later)
    actions.move_by_offset(-x, -y).perform()

        # === Check if one technical asset exists ===
    threagile_data = self.driver.execute_script("return editorUi.editor.graph.model.threagile.toJSON();")
    technical_assets = threagile_data.get("technical_assets", {})

    assert isinstance(technical_assets, dict), "technical_assets is not a dictionary"
    assert len(technical_assets) >= 1, "No technical assets were found after click"


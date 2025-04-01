import pytest
import time
import json
from selenium.webdriver.support.ui import Select
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
    #options.add_argument("--headless=new")  # Or just "--headless"
    options.add_argument("--window-size=1854,1011")


    self.driver = webdriver.Chrome(options)
    self.vars = {}

  
  def teardown_method(self, method):
    self.driver.quit()

  def edit_and_verify_field(self, xpath, input_text, verify_key, verify_field=None, expected_value=None, save_button_xpath=None):
    # Click the edit button
    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()

    # Enter the new text
    active = self.driver.switch_to.active_element
    active.send_keys(Keys.CONTROL, 'a')
    active.send_keys(input_text)

    # If a save/confirm button needs to be clicked
    if save_button_xpath:
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, save_button_xpath))
        ).click()

    # Retrieve updated data
    threagile_data = self.driver.execute_script("return editorUi.editor.graph.model.threagile.toJSON();")
    technical_assets = threagile_data.get("technical_assets", {})
    assert isinstance(technical_assets, dict), "technical_assets is not a dict"
    assert verify_key in technical_assets, f"Expected technical asset key '{verify_key}' not found"

    # Optionally verify a specific field value
    if verify_field and expected_value is not None:
        actual_value = technical_assets[verify_key].get(verify_field)
        assert actual_value == expected_value, f"Expected {verify_field} '{expected_value}', got '{actual_value}'"

  def select_and_assert(self, select_xpath, expected_value, asset_key="foo", attribute="type"):
    """
    Helper to select a value from a <select> and assert that the asset has the expected value for a given attribute.
    """
    select_element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, select_xpath))
    )
    dropdown = Select(select_element)
    dropdown.select_by_visible_text(expected_value)

    # Re-fetch the data to get updated values
    threagile_data = self.driver.execute_script("return editorUi.editor.graph.model.threagile.toJSON();")
    technical_assets = threagile_data.get("technical_assets", {})
    asset = technical_assets.get(asset_key)

    assert asset is not None, f"Technical asset '{asset_key}' not found"
    actual_value = asset.get(attribute)
    assert actual_value == expected_value, f"Expected {attribute} '{expected_value}', but got '{actual_value}'"


  def test_technical_asset(self):
    def relative_click(orig_x, orig_y, ref_width, ref_height, width, height):
        """Helper to calculate position and perform relative click"""
        rel_x = orig_x / ref_width
        rel_y = orig_y / ref_height
        x = int(width * rel_x)
        y = int(height * rel_y)
        actions = ActionChains(self.driver)
        actions.move_by_offset(x, y).click().perform()
        actions.move_by_offset(-x, -y).perform()

    self.driver.get("http://0.0.0.0:8000/indexTests.html")
    self.driver.set_window_size(1854, 1011)
    self.driver.switch_to.frame(0)
    self.driver.find_element(By.CSS_SELECTOR, "td:nth-child(1) > .geBtn").click()
    self.driver.switch_to.default_content()

    window_size = self.driver.get_window_size()
    width, height = window_size['width'], window_size['height']
    ref_width, ref_height = 1854, 1011

    # Click to create asset
    relative_click(1215, 103, ref_width, ref_height, width, height)

    self.edit_and_verify_field(
    xpath="/html/body/div[4]/div[2]/div/div/div[1]/li[1]/button",
    input_text="foo",
    verify_key="foo"
    )

    # Edit description (with a save button)
    self.edit_and_verify_field(
        xpath="/html/body/div[4]/div[2]/div/div/div[1]/li[3]/button",
        input_text="foo",
        verify_key="foo",
        verify_field="description",
        expected_value="foo",
        save_button_xpath="/html/body/div[10]/table/tbody/tr[3]/td/button[2]"
    )

    # === Use helper to test <select> changes ===
    self.select_and_assert("/html/body/div[4]/div[2]/div/div/div[2]/li[1]/div/select", "datastore", "foo", "type")
    self.select_and_assert("/html/body/div[4]/div[2]/div/div/div[2]/li[2]/div/select",  "build-pipeline","foo","technology")
    self.select_and_assert("/html/body/div[4]/div[2]/div/div/div[2]/li[3]/div/select", "system","foo","size"  )
    self.select_and_assert("/html/body/div[4]/div[2]/div/div/div[2]/li[4]/div/select","virtual","foo", "machine"  )
    self.select_and_assert("/html/body/div[4]/div[2]/div/div/div[2]/li[5]/div/select","data-with-symmetric-shared-key", "foo", "encryption", )  
    self.select_and_assert("/html/body/div[4]/div[2]/div/div/div[4]/li[1]/div/select","devops",  "foo","usage", )  


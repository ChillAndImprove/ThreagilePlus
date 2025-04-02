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

  
  def click_and_assert_nested_key_exists(self, click_xpath_1, click_xpath_2, root_key="technical_assets", asset_key="foo", nested_path_prefix=None):
    """
    Clicks two elements, fetches a value from the second, normalizes it, and asserts that a nested key exists.

    :param click_xpath_1: XPath to the first clickable element (e.g., tag input).
    :param click_xpath_2: XPath to the element whose value/text will be used.
    :param root_key: Top-level JSON key (e.g., 'technical_assets').
    :param asset_key: Sub-key under the root (e.g., 'foo').
    :param nested_path_prefix: Optional list of prefix keys before the dynamic key (e.g., ['data_assets_processed']).
    """
    assert isinstance(nested_path_prefix, list), "nested_path_prefix must be a list"

    # Step 1: Click the first element (e.g., open dropdown)
    clickable_1 = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, click_xpath_1))
    )
    clickable_1.click()

    # Step 2: Click the second element (the actual dropdown value)
    clickable_2 = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, click_xpath_2))
    )
    clickable_2.click()

    # Step 3: Extract and normalize value
    value = clickable_2.get_attribute("value") or clickable_2.text
    normalized_value = value.strip().lower().replace(" ", "-")

    # Step 4: Build full nested path
    nested_path = nested_path_prefix + [normalized_value]

    # Step 5: Fetch model data
    threagile_data = self.driver.execute_script("return editorUi.editor.graph.model.threagile.toJSON();")

    current = threagile_data
    try:
        current = current[root_key]
        current = current[asset_key]

        for i, key in enumerate(nested_path):
            if isinstance(current, dict):
                current = current[key]
            elif isinstance(current, list):
                if not isinstance(key, int) or key >= len(current):
                    raise AssertionError(f"Expected index '{key}' in path but list is too short")
                current = current[key]
            else:
                raise AssertionError(f"Unexpected structure at '{key}' in path")

        # If we reached here, key exists ✅
        return
    except KeyError:
        full_path = f"{root_key} -> {asset_key} -> {' -> '.join(map(str, nested_path))}"
        raise AssertionError(f"Expected item to exist at path '{full_path}', but it was not found")


  def click_and_assert_nested_key_removed(self, click_xpath, root_key="technical_assets", asset_key="foo", nested_path=None):
    """
    Clicks an element and asserts that a nested key no longer exists in the data returned from threagile.toJSON().

    :param click_xpath: XPath to the element to be clicked (e.g., 'remove' button).
    :param root_key: Top-level JSON key (e.g., 'technical_assets').
    :param asset_key: Sub-key under the root (e.g., 'foo').
    :param nested_path: List of keys forming the path to the target (e.g., ['data_assets_processed', 'customer-data']).
    """
    assert nested_path and isinstance(nested_path, list), "nested_path must be a non-empty list of keys"

    # Click the element
    clickable = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, click_xpath))
    )
    clickable.click()

    # Wait briefly for the UI/model to update
    self.driver.implicitly_wait(1)

    # Re-fetch model data
    threagile_data = self.driver.execute_script("return editorUi.editor.graph.model.threagile.toJSON();")

    current = threagile_data
    try:
        current = current[root_key]
        current = current[asset_key]

        for i, key in enumerate(nested_path):
            if isinstance(current, dict):
                if key not in current:
                    return  # ✅ key gone
                current = current[key]
            elif isinstance(current, list):
                if not isinstance(key, int) or key >= len(current):
                    return  # ✅ index gone or invalid
                current = current[key]
            else:
                return  # ✅ unexpected structure = also considered gone

        # If we get here, the item still exists — fail
        full_path = f"{root_key} -> {asset_key} -> {' -> '.join(map(str, nested_path))}"
        raise AssertionError(f"Expected item to be removed at path '{full_path}', but it still exists")

    except (KeyError, IndexError, TypeError):
        # ✅ It's gone — either a missing key or index access failure
        return


  def toggle_checkbox_and_assert(self, checkbox_xpath, asset_key="foo", attribute="internet"):
    """
    Generic helper to toggle a checkbox and assert the technical asset's boolean attribute is updated accordingly.
    """
    # Wait until the checkbox is present in the DOM
    checkbox = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, checkbox_xpath))
    )

    # Check current state
    was_checked = checkbox.is_selected()

    # Toggle it
    checkbox.click()

    # Wait a moment if needed (if value updates are async)
    self.driver.implicitly_wait(1)

    # Fetch updated data
    threagile_data = self.driver.execute_script("return editorUi.editor.graph.model.threagile.toJSON();")
    technical_assets = threagile_data.get("technical_assets", {})
    asset = technical_assets.get(asset_key)

    assert asset is not None, f"Technical asset '{asset_key}' not found"

    expected_value = not was_checked
    actual_value = asset.get(attribute)

    assert actual_value == expected_value, (
        f"Expected '{attribute}' to be {expected_value}, but got '{actual_value}'"
    )
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
    #relative_click(1215, 103, ref_width, ref_height, width, height)
    # Get the first cell from the model (excluding the root cell)
    target_label = "Customer Web Client"

    target_cell_id = self.driver.execute_script(f"""
        var graph = editorUi.editor.graph;
        var model = graph.model;
        var root = model.getRoot();

        var childCount = model.getChildCount(root);
        for (var i = 0; i < childCount; i++) {{
            var layer = model.getChildAt(root, i);
            var innerCount = model.getChildCount(layer);
            for (var j = 0; j < innerCount; j++) {{
                var cell = model.getChildAt(layer, j);
                if (cell != null && cell.vertex) {{
                    var label = cell.value;
                    if (typeof label !== "string" && label && label.hasAttribute) {{
                        label = label.getAttribute("label") || label.getAttribute("value");
                    }}
                    if (label === "{target_label}") {{
                        graph.setSelectionCell(cell);
                        graph.scrollCellToVisible(cell);
                        return cell.id;
                    }}
                }}
            }}
        }}
        return null;
    """)  # <---- You were missing this!

    print("Focused node ID:", target_cell_id)

    self.edit_and_verify_field(
    xpath="/html/body/div[4]/div[2]/div/div/div[1]/li[1]/button",
    save_button_xpath="/html/body/div[10]/table/tbody/tr[3]/td/button[2]",
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
    
    self.toggle_checkbox_and_assert(  checkbox_xpath="/html/body/div[4]/div[2]/div/div/div[4]/div[1]/input",     asset_key="foo",  attribute="used_as_client_by_human" )
    self.toggle_checkbox_and_assert(  checkbox_xpath="/html/body/div[4]/div[2]/div/div/div[4]/div[2]/input",     asset_key="foo",  attribute="multi_tenant" )
    self.toggle_checkbox_and_assert(  checkbox_xpath="/html/body/div[4]/div[2]/div/div/div[4]/div[3]/input",     asset_key="foo",  attribute="redundant" )
    self.toggle_checkbox_and_assert(  checkbox_xpath="/html/body/div[4]/div[2]/div/div/div[4]/div[4]/input",     asset_key="foo",  attribute="custom_developed_parts" )
    self.toggle_checkbox_and_assert(  checkbox_xpath="/html/body/div[4]/div[2]/div/div/div[4]/div[5]/input",     asset_key="foo",  attribute="out_of_scope" )
    self.edit_and_verify_field(
        xpath="/html/body/div[4]/div[2]/div/div/div[4]/li[2]/button",
        input_text="foo",
        verify_key="foo",
        verify_field="justification_out_of_scope",
        expected_value="foo",
        save_button_xpath="/html/body/div[10]/table/tbody/tr[3]/td/button[2]"
    )

    
    self.click_and_assert_nested_key_removed(
        click_xpath="/html/body/div[4]/div[2]/div/div/div[5]/tags/tag[1]/x",
        
        root_key="technical_assets",
        asset_key="foo",
        nested_path=["data_assets_processed", "customer-contracts"]
    )
    self.click_and_assert_nested_key_removed(
        click_xpath="/html/body/div[4]/div[2]/div/div/div[5]/tags/tag[1]/x",
        root_key="technical_assets",
        asset_key="foo",
        nested_path=["data_assets_processed", "customer-operational-data"]
    )
    self.click_and_assert_nested_key_removed(
        click_xpath="/html/body/div[4]/div[2]/div/div/div[5]/tags/tag[1]/x",
        
        root_key="technical_assets",
        asset_key="foo",
        nested_path=["data_assets_processed", "customer-accounts"]
    )
    self.click_and_assert_nested_key_removed(
        click_xpath="/html/body/div[4]/div[2]/div/div/div[5]/tags/tag[1]/x",
        
        root_key="technical_assets",
        asset_key="foo",
        nested_path=["data_assets_processed", "customer-application-code"]
    )
    self.click_and_assert_nested_key_removed(
        click_xpath="/html/body/div[4]/div[2]/div/div/div[5]/tags/tag[1]/x",
        root_key="technical_assets",
        asset_key="foo",
        nested_path=["data_assets_processed", "client-application-code"]
    )

    self.click_and_assert_nested_key_exists(
        click_xpath_1='/html/body/div[4]/div[2]/div/div/div[5]/tags/span',
        click_xpath_2='/html/body/div[9]/div/div[1]',
        root_key='technical_assets',
        asset_key='foo',
        nested_path_prefix=['data_assets_processed']
    )



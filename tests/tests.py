import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

user_name = os.getlogin()
file_path = f"/home/{user_name}/ThreagilePlus/wasm/Threagile/threagile.yaml"

class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.url = "localhost:8000/indexTest.html"
        cls.driver.get(cls.url)
        print()
        print()
        print()
        print()
        print("Starting...")
        cls.import_file(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # Setters
    def click_checkbox_and_execute_script(self,click_selector, checkbox_selector, script, expected_value, msg):
        try:
            element_to_click = self.driver.find_element(By.CSS_SELECTOR, click_selector)
            element_to_click.click()

            checkbox_element = self.wait_for_element_to_be_clickable(checkbox_selector)
 
            old =checkbox_element.is_selected()
            checkbox_element.click()
            value = self.driver.execute_script(script)
            self.assertEqual(value, str(not bool(old)).lower(), msg=msg)
        except Exception as e:
            print(f"Test failed with error: {e}")
            raise


    def get_background_color(self, css_selector):
        """Returns the background color of the element."""
        element = self.driver.find_element(By.CSS_SELECTOR, css_selector)
        return element.value_of_css_property('background-color')

    def click_button_and_execute_script_data_assets(self, click_selector, button_selector, script, expected_value, text_area):                                                                                                                             
        try:                                                                                                                                                                                                                                  
            self.driver.execute_script("return window.editorUi.editor.graph.clearSelection();")
            
            bg_color_selector = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4)"
            if self.get_background_color(bg_color_selector) == "rgb(211, 211, 211)":  # This is the RGBA value for lightgray
                WebDriverWait(self.driver, 0.5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, click_selector))).click()
                button = WebDriverWait(self.driver, 0.5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))

            # Try to locate the button without clicking click_selector
            else:
                try:
                    button = WebDriverWait(self.driver, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, button_selector)))
                except TimeoutException:
                    pass

            # Click the button
            button.click()

            # Work with the textarea
            textarea_input = self.driver.find_element(By.CSS_SELECTOR, text_area)
            textarea_content = textarea_input.text
            textarea_input.send_keys("foo")

            # Execute the script and validate
            value = self.driver.execute_script(script)
            self.assertEqual(value, expected_value, msg=f"The value is not set to '{expected_value}'")

            # Close the dialog or popup or whatever the button represents
            close = self.driver.find_element(By.CSS_SELECTOR, "button.geBtn:nth-child(1)")
            close.click()

        except Exception as e:
            print("Exception:", e)
            close = self.driver.find_element(By.CSS_SELECTOR, "button.geBtn:nth-child(1)")
            close.click()


    def click_button_and_execute_script(self, click_selector, button_selector, script, expected_value, text_area):                                                                                                                             
        try:                                                                                                                                                                                                                                  
            # Warte, bis das Element zum Anklicken vorhanden ist und dann klicke darauf
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, click_selector))).click()

            # Warte, bis das Button-Element vorhanden ist und dann klicke darauf
            button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, button_selector)))
            button.click()

            textarea_input = self.driver.find_element(By.CSS_SELECTOR, text_area)
            textarea_content = textarea_input.text
            textarea_input.send_keys("foo")

            value = self.driver.execute_script(script)
            self.assertEqual(value, expected_value, msg=f"The value is not set to '{expected_value}'")

            close = self.driver.find_element(By.CSS_SELECTOR, "button.geBtn:nth-child(1)")
            close.click()

        except Exception as e:
            print("Exception:", e)
            close= self.driver.find_element(By.CSS_SELECTOR, "button.geBtn:nth-child(1)")
            close.click()

    def test_trust_boundaries_set_type(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['trust_boundaries','Application Network','type']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(4) > g:nth-child(1) > text:nth-child(1)"
        option_text = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > li:nth-child(2) > div:nth-child(2) > select:nth-child(1)"
        self.select_option_and_execute_script(click_selector, option_text, 'network-cloud-security-group', script, 'network-cloud-provider')

    def select_option_and_execute_script_data_assets(self, click_selector, select_selector, option_text, script, expected_value):
        try:
            self.driver.execute_script("return window.editorUi.editor.graph.clearSelection();")
            
            bg_color_selector = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4)"
            if self.get_background_color(bg_color_selector) == "rgb(211, 211, 211)":  # This is the RGBA value for lightgray
                WebDriverWait(self.driver, 0.5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, click_selector))).click()
                select_element = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, select_selector)))

            # Try to locate the select_element without clicking click_selector
            else:
                try:
                    select_element = WebDriverWait(self.driver, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, select_selector)))
                except TimeoutException:
                    pass
            
            # Select the option
            select = Select(select_element)
            select.select_by_visible_text(option_text)
                
            # Execute the script
            value = self.driver.execute_script(script)
            self.assertEqual(value, expected_value, msg=f"The value is not set to '{expected_value}'")
                
        except Exception as e:
            print(f"Exception: {e}")
            raise 
 

    def select_option_and_execute_script(self, click_selector, select_selector, option_text, script, expected_value):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, click_selector))).click()

            select_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, select_selector)))
            select = Select(select_element)
            select.select_by_visible_text(option_text)

            value = self.driver.execute_script(script)
            self.assertEqual(value, expected_value, msg=f"The value is not set to '{expected_value}'")

        except Exception as e:
            print(f"Exception: {e}")
            raise
 
    def test_trust_boundary_set_title(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['trust_boundaries','Application Network','description']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(4) > g:nth-child(1) > text:nth-child(1)"
        button = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > li:nth-child(1) > button:nth-child(1)"
        textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
        name = "Application Network"
        self.click_button_and_execute_script(click_selector, button,  script, "foo"+name,textarea)
 
    def test_trust_boundary_set_description(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['trust_boundaries','Application Network','description']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(4) > g:nth-child(1) > text:nth-child(1)"
        button = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > li:nth-child(2) > button:nth-child(1)"
        textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
        name = "Application Network"
        self.click_button_and_execute_script(click_selector, button,  script, "foo"+name,textarea)
 
    def test_trust_boundary_set_id(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['trust_boundaries','Application Network','id']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(4) > g:nth-child(1) > text:nth-child(1)"
        button = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > li:nth-child(1) > button:nth-child(1)"
        textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
        name = "application-network"
        self.click_button_and_execute_script(click_selector, button,  script, "foo"+name,textarea)
 
    def test_technical_assets_set_id(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','description']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        button = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(2) > button:nth-child(1)"
        textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
        name = "external-dev-client"
        self.click_button_and_execute_script(click_selector, button,  script, "foo"+name,textarea)
    def test_technical_assets_set_owner(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','description']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        button = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > li:nth-child(6) > button:nth-child(1)"
        textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
        name = "External Developers"
        self.click_button_and_execute_script(click_selector, button,  script, "foo"+name,textarea)

    def test_technical_assets_set_justification(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','description']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        button = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > li:nth-child(7) > button:nth-child(1)"
        textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
        name = "Owned and managed by external developers"
        self.click_button_and_execute_script(click_selector, button,  script, "foo"+name,textarea)


    def test_technical_assets_set_description(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','description']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        button = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > li:nth-child(1) > button:nth-child(1)"
        textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
        name = "External developer client"
        self.click_button_and_execute_script(click_selector, button,  script, "foo"+name,textarea)

    def test_technical_assets_set_confidential(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','confidentiality']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        option_text = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > li:nth-child(1) > div:nth-child(2) > select:nth-child(1)"
        self.select_option_and_execute_script(click_selector, option_text, 'internal', script, 'Public')

    def test_technical_assets_set_integrity(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','integrity']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        option_text = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > li:nth-child(2) > div:nth-child(2) > select:nth-child(1)"
        self.select_option_and_execute_script(click_selector, option_text, 'archive', script, 'Archive')
    
    def test_technical_assets_set_availability(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','availability']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        option_text = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > li:nth-child(3) > div:nth-child(2) > select:nth-child(1)"
        self.select_option_and_execute_script(click_selector, option_text, 'archive', script, 'Archive')

    def test_technical_assets_set_usage(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','usage']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        option_text = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > li:nth-child(1) > div:nth-child(2) > select:nth-child(1)"
        self.select_option_and_execute_script(click_selector, option_text, 'business', script, 'business')

    def test_technical_assets_set_type(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','type']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        option_text = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > li:nth-child(1) > div:nth-child(2) > select:nth-child(1)"
        self.select_option_and_execute_script(click_selector, option_text, 'process', script, 'process')

    def test_technical_assets_set_technology(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','technology']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        option_text = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > li:nth-child(2) > div:nth-child(2) > select:nth-child(1)"
        self.select_option_and_execute_script(click_selector, option_text, 'browser', script, 'browser')
    def test_technical_assets_set_size(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','size']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        option_text = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > li:nth-child(3) > div:nth-child(2) > select:nth-child(1)"
        self.select_option_and_execute_script(click_selector, option_text, 'service', script, 'service')
    def test_technical_assets_set_machine(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','machine']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        option_text = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > li:nth-child(4) > div:nth-child(2) > select:nth-child(1)"
        self.select_option_and_execute_script(click_selector, option_text, 'virtual', script, 'virtual')
    def test_technical_assets_set_encryption(self):
        script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','encryption']);"
        click_selector =".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        option_text = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > li:nth-child(5) > div:nth-child(2) > select:nth-child(1)"
        self.select_option_and_execute_script(click_selector, option_text, 'data-with-asymmetric-shared-key', script, 'data-with-asymmetric-shared-key')







    def wait_for_element_to_be_clickable(self, selector, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    def test_technical_assets_set_internet(self):
        element_selector = ".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        checkbox_selector = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(7) > input:nth-child(1)"
        script = "var result = window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','internet']); return result;"
        expected_value = 'false'
        self.click_checkbox_and_execute_script(element_selector, checkbox_selector, script, expected_value, msg="The value is not set to 'false'")

    def test_technical_assets_set_used_as_client_by_human(self):
        element_selector = ".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        checkbox_selector = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(2) > input:nth-child(1)"
        script = "var result = window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','used_as_client_by_human']); return result;"
        expected_value = 'false'
        self.click_checkbox_and_execute_script(element_selector, checkbox_selector, script, expected_value, msg="The value is not set to 'false'")
    def test_technical_assets_set_redudant(self):
        element_selector = ".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        checkbox_selector = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(4) > input:nth-child(1)"
        script = "var result = window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','redudant']); return result;"
        expected_value = 'false'
        self.click_checkbox_and_execute_script(element_selector, checkbox_selector, script, expected_value, msg="The value is not set to 'false'")
    def test_technical_assets_set_custom_develop_parts(self):
        element_selector = ".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        checkbox_selector = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(5) > input:nth-child(1)"
        script = "var result = window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','custom_develop_parts']); return result;"
        expected_value = 'false'
        self.click_checkbox_and_execute_script(element_selector, checkbox_selector, script, expected_value, msg="The value is not set to 'false'")
    def test_technical_assets_set_out_of_scope(self):
        element_selector = ".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        checkbox_selector = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(6) > input:nth-child(1)"
        script = "var result = window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','out_of_scope']); return result;"
        expected_value = 'false'
        self.click_checkbox_and_execute_script(element_selector, checkbox_selector, script, expected_value, msg="The value is not set to 'false'")




    def test_technical_assets_set_multi_tenant(self):
        element_selector = ".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)"
        checkbox_selector = "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > div:nth-child(3) > input:nth-child(1)"
        script = "var result = window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','multi_tenant']); return result;"
        expected_value = 'false'
        self.click_checkbox_and_execute_script(element_selector, checkbox_selector, script, expected_value, msg="The value is not set to 'false'")



    def import_file(cls):
        try:
            time.sleep(1)
            
            # Click on "File"
            file_menu = cls.driver.find_element(By.CSS_SELECTOR, "div.geMenubar a.geItem:nth-child(1)")
            file_menu.click()
            
            time.sleep(1)
            # Find and click on "Import..."
            menu_items = cls.driver.find_elements(By.CSS_SELECTOR, "td.mxPopupMenuItem[align='left']")
            found_import = False
            for item in menu_items:
                if item.text == "Import...":
                    item.click()
                    found_import = True
                    break
    
            iframe = cls.driver.find_element(By.CSS_SELECTOR, "iframe[width='320px']")
            cls.driver.switch_to.frame(iframe)
            input_element = cls.driver.find_element(By.CSS_SELECTOR, "#openForm > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)")
            input_element.send_keys(file_path)
            import_button = cls.driver.find_element(By.CSS_SELECTOR, "#openButton")
            import_button.click()
            # time.sleep(10)
            cls.driver.switch_to.default_content()
        finally:
            print("Setup succeeded" + u'\u2713')


    def test_add_data_asset(self):
            script = """
             var result =window.editorUi.editor.graph.model.threagile.getIn(['data_assets']).items.length;  
             return result;
             """
            old = self.driver.execute_script(script)
            add_data = self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > button:nth-child(2)")
            add_data.click()
            script = """
             var result =window.editorUi.editor.graph.model.threagile.getIn(['data_assets']).items.length;  
             return result;
             """
            new = self.driver.execute_script(script)
            self.assertEqual(new,old+1 , msg="No data asset added")

    def test_delete_data_asset(self):
            tmp = self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(5) > div:nth-child(4) > div:nth-child(1) > a:nth-child(3) > svg:nth-child(1) > g:nth-child(1) > g:nth-child(2) > g:nth-child(2) > g:nth-child(1) > foreignObject:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
            tmp.click()
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.DELETE)  # Press the delete key
            actions.perform()
            data = self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1) > img:nth-child(1)")
            data.click()
            script = """
             var result =window.editorUi.editor.graph.model.threagile.getIn(['data_assets']).items.length;  
             return result;
             """
            old = self.driver.execute_script(script)
            deleteButton = self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1) > button:nth-child(3)")
            deleteButton.click()           
            script = """
             var result =window.editorUi.editor.graph.model.threagile.getIn(['data_assets']).items.length;  
             return result;
             """
            new = self.driver.execute_script(script)
              
            self.assertEqual(new,old-1 , msg="No data asset deleted")
    
    def test_data_justification_cia_rating(self):
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['data_assets','Customer Accounts','justification_cia_rating']);"
            click_selector ="div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > img:nth-child(1)"
            button = "#Customer\ Accounts > div:nth-child(1) > li:nth-child(11) > button:nth-child(1)"
            textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
            name = "Customer account data for using the portal are required to be available to offer the portal functionality."
            self.click_button_and_execute_script_data_assets(click_selector, button,  script, "foo"+name,textarea)
    def test_data_asset_integrity(self):
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['data_assets','Customer Accounts','integrity']);"
            click_selector ="div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > img:nth-child(1)"
            option_text = "#Customer\ Accounts > div:nth-child(1) > li:nth-child(9) > div:nth-child(2) > select:nth-child(1)"
            self.select_option_and_execute_script_data_assets(click_selector, option_text, 'important', script, 'operational')

    def test_data_asset_usage(self):
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['data_assets','Customer Accounts','usage']);"
            click_selector ="div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > img:nth-child(1)"
            option_text = "#Customer\ Accounts > div:nth-child(1) > li:nth-child(3) > div:nth-child(2) > select:nth-child(1)"
            self.select_option_and_execute_script_data_assets(click_selector, option_text, 'devops', script, 'business')



    def test_data_asset_availability(self):
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['data_assets','Customer Accounts','availability']);"
            click_selector ="div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > img:nth-child(1)"
            option_text = "#Customer\ Accounts > div:nth-child(1) > li:nth-child(10) > div:nth-child(2) > select:nth-child(1)"
            self.select_option_and_execute_script_data_assets(click_selector, option_text, 'important', script, 'operational')


    def test_data_asset_confidentiality(self):
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['data_assets','Customer Accounts','confidentiality']);"
            click_selector ="div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > img:nth-child(1)"
            option_text = "#Customer\ Accounts > div:nth-child(1) > li:nth-child(8) > div:nth-child(2) > select:nth-child(1)"
            self.select_option_and_execute_script_data_assets(click_selector, option_text, 'internal', script, 'strictly-confidential')


    def test_data_asset_quantity(self):
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['data_assets','Customer Accounts','quantity']);"
            click_selector ="div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > img:nth-child(1)"
            option_text = "#Customer\ Accounts > div:nth-child(1) > li:nth-child(7) > div:nth-child(2) > select:nth-child(1)"
            self.select_option_and_execute_script_data_assets(click_selector, option_text, 'very-few', script, 'many')


    def test_data_asset_owner(self):
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['data_assets','Customer Accounts','description']);"
            click_selector ="div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > img:nth-child(1)"
            button = "#Customer\ Accounts > div:nth-child(1) > li:nth-child(6) > button:nth-child(1)"
            textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
            name = "Customer"
            self.click_button_and_execute_script_data_assets(click_selector, button,  script, "foo"+name,textarea)


    def test_data_asset_origin(self):
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['data_assets','Customer Accounts','description']);"
            click_selector ="div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > img:nth-child(1)"
            button = "#Customer\ Accounts > div:nth-child(1) > li:nth-child(5) > button:nth-child(1)"
            textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
            name = "Customer"
            self.click_button_and_execute_script_data_assets(click_selector, button,  script, "foo"+name,textarea)

    def test_data_asset_description(self):
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['data_assets','Customer Accounts','description']);"
            click_selector ="div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > img:nth-child(1)"
            button = "#Customer\ Accounts > div:nth-child(1) > li:nth-child(2) > button:nth-child(1)"
            textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
            name = "Customer Accounts (including transient credentials when entered for checking them)"
            self.click_button_and_execute_script_data_assets(click_selector, button,  script, "foo"+name,textarea)
     


    def test_data_asset_id(self):
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['data_assets','Customer Accounts','id']);"
            click_selector ="div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(4) > div:nth-child(1) > img:nth-child(1)"
            button = "#Customer\ Accounts > div:nth-child(1) > li:nth-child(1) > button:nth-child(1)"
            textarea=".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)"
            name = "customer-accounts"
            self.click_button_and_execute_script_data_assets(click_selector, button,  script, "foo"+name,textarea)
     




    def test_check_connection(self):
            script = """
                var graph = window.editorUi.editor.graph;
                var parent = graph.getDefaultParent();
                var vertices = graph.getChildVertices(parent);


                var sourceVertex = null;
                var targetVertex = null;

                vertices.forEach(function(vertex) {
                  if (vertex.value === 'Jenkins Buildserver') {
                    sourceVertex = vertex;
                  }
                  if (vertex.value === 'Customer Web Client') {
                    targetVertex = vertex;
                  }
                });

                if (sourceVertex && targetVertex) {
                    var edge = graph.insertEdge(parent, null, '', sourceVertex, targetVertex);
                    graph.refresh();
                    return {
                        source: sourceVertex.value,
                        target: targetVertex.value,
                        edge: edge.id
                    };
                }
            """
            value2 = self.driver.execute_script(script)
            script2 = """
             var result =window.editorUi.editor.graph.model.threagile.getIn(['technical_assets', 'Jenkins Buildserver', 'communication_links','Customer Web Client Access']);  
             return result;
             """
            value = self.driver.execute_script(script2)
            self.assertEqual(None,value , msg="Didn't work")



    def test_technical_assets_import_confidential(self):
        try:
            # Click on the specified element
            element_to_click = self.driver.find_element(By.CSS_SELECTOR, ".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)")
            element_to_click.click()

            time.sleep(2) # Wait to allow the dropdown to load

            # Find the select element
            select_element = self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > li:nth-child(1) > div:nth-child(2) > select:nth-child(1)")
            # Use the Select class to choose "confidential" from the dropdown
            select = Select(select_element)

            # Check that "confidential" was indeed selected
            selected_option = select.first_selected_option
            self.assertEqual(selected_option.text, 'confidential', msg="The 'confidential' option was not selected")

        except Exception as e:
            print(f"Test failed with error: {e}")
            raise
    def test_technical_assets_set_data_processed(self):
        try:
            # Click on the specified element
            element_to_click = self.driver.find_element(By.CSS_SELECTOR, ".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)")
            element_to_click.click()

            time.sleep(2) # Wait to allow the dropdown to load

            delete_button= self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > tags:nth-child(2) > tag:nth-child(1) > x:nth-child(1)")
            delete_button.click()            
            script = """
             var result = window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','data_assets_processed']);
            return result;
             """
            value = self.driver.execute_script(script)
            self.assertEqual(1, len(value), msg="There is not one object left.")


        except Exception as e:
            print(f"Test failed with error: {e}")
            raise




    def test_zata_assets(self):
        try:
            tmp = self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(5) > div:nth-child(4) > div:nth-child(1) > a:nth-child(3) > svg:nth-child(1) > g:nth-child(1) > g:nth-child(2) > g:nth-child(2) > g:nth-child(1) > foreignObject:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)")
            tmp.click()
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.DELETE)  # Press the delete key
            actions.perform()
            time.sleep(2)
            first_element = self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(2) > div:nth-child(1) > img:nth-child(1)")
            first_element.click()

            time.sleep(2)

            second_element = self.driver.find_element(By.CSS_SELECTOR, "#Customer\ Contract\ Summaries > div:nth-child(1) > li:nth-child(1) > button:nth-child(1)")
            second_element.click()

            time.sleep(2)

            textarea_content = self.driver.find_element(By.CSS_SELECTOR, ".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)").text

            self.assertNotEqual(textarea_content, "E.g. Element1", msg="Unexpected content in the textarea")
            close_button = self.driver.find_element(By.CSS_SELECTOR, "button.geBtn:nth-child(1)")
            close_button.click()

        except Exception as e:
            print(f"Test failed with error: {e}")
            close_button = self.driver.find_element(By.CSS_SELECTOR, "button.geBtn:nth-child(1)")
            close_button.click()
            raise


if __name__ == "__main__":
    unittest.main()

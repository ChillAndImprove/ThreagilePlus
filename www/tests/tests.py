import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
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
        cls.import_file(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


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
            time.sleep(10)
            cls.driver.switch_to.default_content()
        finally:
            print("done")

    def test_acheck_connection(self):
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



    def test_technical_assets_set_internet(self):
        try:
            # Click on the specified element
            element_to_click = self.driver.find_element(By.CSS_SELECTOR, ".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)")
            element_to_click.click()

            time.sleep(2) # Wait to allow the dropdown to load

            checkbox_element = self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(7) > input:nth-child(1)")
            checkbox_element.click()            
            # Check that "confidential" was indeed selected
            script = """
             var result = window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','internet']);
            return result;
             """
            value = self.driver.execute_script(script)
            self.assertEqual(value, 'false', msg="The value is not set to 'false'")


        except Exception as e:
            print(f"Test failed with error: {e}")
            raise


    def test_technical_assets_set_confidential(self):
        try:
            # Click on the specified element
            element_to_click = self.driver.find_element(By.CSS_SELECTOR, ".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)")
            element_to_click.click()

            time.sleep(2) # Wait to allow the dropdown to load

            # Find the select element
            select_element = self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > li:nth-child(1) > div:nth-child(2) > select:nth-child(1)")

            # Use the Select class to choose "confidential" from the dropdown
            from selenium.webdriver.support.ui import Select
            select = Select(select_element)
            select.select_by_visible_text('internal')

            # Check that "confidential" was indeed selected
            selected_option = select.first_selected_option
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','confidentiality']);"
            value = self.driver.execute_script(script)
            self.assertEqual(value, 'Public', msg="The value is not set to 'Public'")


        except Exception as e:
            print(f"Test failed with error: {e}")
            raise



    def test_technical_assets_set_confidential(self):
        try:
            # Click on the specified element
            element_to_click = self.driver.find_element(By.CSS_SELECTOR, ".geDiagramContainer > svg:nth-child(2) > g:nth-child(1) > g:nth-child(2) > g:nth-child(36) > g:nth-child(1) > text:nth-child(1)")
            element_to_click.click()

            time.sleep(2) # Wait to allow the dropdown to load

            # Find the select element
            select_element = self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > li:nth-child(1) > div:nth-child(2) > select:nth-child(1)")

            # Use the Select class to choose "confidential" from the dropdown
            from selenium.webdriver.support.ui import Select
            select = Select(select_element)
            select.select_by_visible_text('internal')

            # Check that "confidential" was indeed selected
            selected_option = select.first_selected_option
            script = "return window.editorUi.editor.graph.model.threagile.getIn(['technical_assets','External Development Client','confidentiality']);"
            value = self.driver.execute_script(script)
            self.assertEqual(value, 'Public', msg="The value is not set to 'Public'")


        except Exception as e:
            print(f"Test failed with error: {e}")
            raise

    def test_zata_assets(self):
        try:
            time.sleep(2)
            
            first_element = self.driver.find_element(By.CSS_SELECTOR, "div.geSidebarContainer:nth-child(6) > div:nth-child(2) > div:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > div:nth-child(1) > img:nth-child(1)")
            first_element.click()

            time.sleep(2)

            second_element = self.driver.find_element(By.CSS_SELECTOR, "#Customer\ Contracts > div:nth-child(1) > li:nth-child(1) > button:nth-child(1)")
            second_element.click()

            time.sleep(2)

            textarea_content = self.driver.find_element(By.CSS_SELECTOR, ".geDialog > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > textarea:nth-child(1)").text

            self.assertNotEqual(textarea_content, "E.g. Element1", msg="Unexpected content in the textarea")
            close_button = self.driver.find_element(By.CSS_SELECTOR, "button.geBtn:nth-child(1)")
            close_button.click()

        except Exception as e:
            print(f"Test failed with error: {e}")
            raise


if __name__ == "__main__":
    unittest.main()
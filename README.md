<p align="center">
  <img src="./www/images/logo.png" alt="Threagile Plus Logo" width="200">
</p>


# Threagile Plus

Welcome to Threagile Plus! This open-source project aims to enhance your experience with threat modeling.

![showcase](finished.gif)

# Project Status

The current state of this project is somewhat challenging. At this point in time, the codebase contains a considerable number of bugs that need attention.

I find myself unable to dedicate the required time to address these bugs promptly. 

I am looking forward to dedicating more time to this project in the near future.

## Getting Started

To start using Threagile Plus, follow these steps:

1. Navigate to the `www` directory:
    ```bash
    cd www
    ```
2. Start the server using Python:
    ```bash
    python3 -m http.server
    ```
3. Open your web browser and go to `http://localhost:8000`.

## Technical Details

Threagile Plus is built upon JGraph (also known as [mxGraph](https://github.com/jgraph/mxgraph)) and [Threagile](https://github.com/Threagile/threagile), which was compiled to WebAssembly (WASM). The combination of these technologies allows for an enhanced and intuitive experience with threat modeling.

## Privacy and Security

I understand the importance of privacy and security, especially when it comes to something as critical as threat modeling. I want to assure you that your threat models are not being sent anywhere. 

This application is purely static JavaScript. All processing is done locally on your machine, and no data is sent out. You can verify this yourself by inspecting the network traffic in your browser.


## TODOs
Tests: 
- Next up tests fürs Verbinden von vertices
	Dafür brauch ich hovern und 
	from selenium.webdriver.common.action_chains import ActionChains

	element_to_hover = driver.find_element_by_css_selector("Element")
	hover_action = ActionChains(driver).move_to_element(element_to_hover)
	hover_action.perform()

	dragg:
	from selenium.webdriver.common.action_chains import ActionChains

	element_to_drag = driver.find_element_by_css_selector("element")
	target_location = driver.find_element_by_css_selector("target")

	drag_and_drop_action = ActionChains(driver).drag_and_drop(element_to_drag, target_location)
	drag_and_drop_action.perform()
- Data Asset 
	- Element löschen
	- Elemente hinzufügen
	- Set
		- Tag
		- Dropdown Menü
		- Buttonz.b description

- Trust Boundary
	- Set
		- Button
		- Dropdown
		- Elemente raus bewegen und reinbewegen
- Check Risks readonly
- Check RiskTracking readonly


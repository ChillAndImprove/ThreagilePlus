<p align="center">
  <img src="./images/logo.png" alt="Threagile Plus Logo" width="200">
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
- Technical Assets
	- Test everthing 	
- Data Asset 
	- Set
		- Tag
		- Dropdown Menü
		- Buttonz.b description

- Trust Boundary
	- Set
		- Button
		- Dropdown
		- Elemente raus bewegen und reinbewegen
- Connections
	- We can click on an edge via js and then check those values
 
- Check Risks readonly
-[REMOVE this] Check RiskTracking readonly
- Check if ID change, changes the value too.
     - Check if Id changes, in other assets the id changes too
- Data Asset, check if id changes in other assets too via test
- Teste Title data assets 

More testing:
Testing the ability to create a graph from scratch(First we gonna just use dummy values in the yaml, like foo and so on for business critically)
- New Element is the graph creating a element with that value in technical Asset
- Same goes for data asset
- Same goes for edges



Bug:
 [X]Github Pages common.js is not loaded because mxgraph tries to find the css from /src/ but that should be /ThreagilePlus.. 

TODO:
- Add title to datasset und zu techical asset,
- Add gauge for how many risks are mitigated

Food for thought:
- How do we work with changes in trust boundaries

<p align="center">
  <img src="./www/images/logo.png" alt="Threagile Plus Logo" width="200">
</p>


# Threagile Plus

Welcome to Threagile Plus! This open-source project, developed solely by me (vacation project), aims to enhance your experience with threat modeling.

![showcase](finished.gif)

# Project Status

I would like to kindly inform you that the current state of this project is somewhat challenging. At this point in time, the codebase contains a considerable number of bugs that need attention.

I find myself unable to dedicate the required time to address these bugs promptly. 

I am looking forward to dedicating more time to this project in the near future. Until then, contributions or even issue reports from you will be highly appreciated to help improve the project.

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

Threagile Plus is built upon JGraph (also known as mxGraph) and Threagile, which was compiled to WebAssembly (WASM). The combination of these technologies allows for an enhanced and intuitive experience with threat modeling.

## Privacy and Security

I understand the importance of privacy and security, especially when it comes to something as critical as threat modeling. I want to assure you that your threat models are not being sent anywhere. 

This application is purely static JavaScript. All processing is done locally on your machine, and no data is sent out. You can verify this yourself by inspecting the network traffic in your browser.

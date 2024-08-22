<p align="center">
  <img src="./images/logo.png" alt="Threagile Plus Logo" width="200">
</p>


# Threagile Plus

Welcome to Threagile Plus! This open-source project aims to enhance your experience with threat modeling.

![showcase](finished.gif)

# Project Status

The current state of this project is somewhat challenging. At this point in time, the codebase contains a considerable number of bugs that need attention.

I find myself unable to dedicate the required time to address these bugs promptly. 

## Getting Started

To start using Threagile Plus, follow these steps:

1. Switch to the cloned repository directory:
    ```bash
    cd path/to/cloned_repo
    ```
2. Launch the server using Python:
    ```bash
    python3 -m http.server
    ```
3. Open your web browser and navigate to `http://localhost:8000`.

4. Click on **File** -> **Import** -> **Browse**. Select your `Threagile.yaml` file and click **Import**.

## Technical Details

Threagile Plus is built upon JGraph (also known as [mxGraph](https://github.com/jgraph/mxgraph)) and [Threagile](https://github.com/Threagile/threagile), which was compiled to WebAssembly (WASM). The combination of these technologies allows for an enhanced and intuitive experience with threat modeling.

## Privacy and Security

I understand the importance of privacy and security, especially when it comes to something as critical as threat modeling. I want to assure you that your threat models are not being sent anywhere.

This application is purely static JavaScript. All processing is done locally on your machine, and no data is sent out. You can verify this yourself by inspecting the network traffic in your browser. Additionally, for enhanced security, you could use a Linux firewall like OpenSnitch or corresponding firewalls on other operating systems to monitor and control outgoing connections, ensuring that no data is inadvertently transmitted.


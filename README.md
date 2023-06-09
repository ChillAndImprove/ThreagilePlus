# Threagile Plus

Welcome to Threagile Plus! This open-source project, developed solely by me (vacation project), aims to enhance your experience with threat modeling.

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

Threagile Plus is built upon JGraph (now known as mxGraph) and Threagile, which was compiled to WebAssembly (WASM). It showcases how these powerful technologies can be utilized to create a highly effective threat modeling tool.

## Privacy and Security

I understand the importance of privacy and security, especially when it comes to something as critical as threat modeling. I want to assure you that your threat models are not being sent anywhere. 

This application is purely static JavaScript. All processing is done locally on your machine, and no data is sent out. You can verify this yourself by inspecting the network traffic in your browser's developer tools.

Furthermore, being an open source project, the code is fully transparent and open for review. This means you (and anyone else) can take a look and make sure there's no funny business happening. 

I encourage you to review the code and see for yourself! 

If you have any questions, issues, or suggestions, feel free to open an issue. I highly value your input and feedback.

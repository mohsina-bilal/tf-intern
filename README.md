# tf-intern

FastAPI for Different Hugging Face Models

This repository contains a FastAPI server that acts as an interface to various deployed Hugging Face models such as text-generation, zero-shot-classification, object-detection, and token-classification.
How to run the server

    Clone this repository.

    Navigate to the directory containing main.py.

    Run the following command in your terminal to start the server. Replace N with the number corresponding to the model you want to use (1 - Text Generation, 2 - Zero Shot Classification, 3 - Object Detection, 4 - Token Classification):

bash

python main.py N

The server will start running on http://localhost:8000.
How to make predictions

Use the /predict endpoint to make POST requests with the appropriate inputs for the chosen model. The input data formats for each model are as follows:
Zero-shot Classification

Request:

json

{
  "inputs": {
    "sequence": "text_sequence",
    "candidate_labels": ["label1", "label2", ..., "labelN"]
  }
}

Object Detection

Request:

json

{
  "inputs": "image.jpg"
}

Token Classification

Request:

json

{
  "inputs": "text_input"
}

Text Generation

Request:

json

{
  "inputs": "text_input"
}

You can make these requests using a tool like curl, Postman, or any HTTP client in a programming language of your choice.
Contributing

Please feel free to open an issue or a pull request if you have any suggestions or find any bugs.


Note: Always remember to replace the model URL and HF pipeline variable with your own information in the main.py file.

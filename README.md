# FastAPI Model Inference Server

This is a FastAPI application that provides an HTTP endpoint for running predictions using several machine-learning models.

## Overview

This application supports four types of pipelines: text generation, zero-shot-classification, object detection, and token classification. It converts input data into the v2 format and sends HTTP POST requests to the model servers to run the inference.

## Setup and Installation

To get started with the application, follow the steps below:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/<mohsina-bilal>/<tf-intern>.git
```

2. Navigate into the folder:

```bash
cd <tf-intern>
```

3. Make sure you have Python 3.6+ installed on your machine. Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

To start the server, run the following command:

```bash
uvicorn app:app
```

Once the server is running, you can send HTTP POST requests to the `/predict` endpoint to run inference on the models. The request body should be a JSON object with a single `inputs` key, whose value can be anything.

Here is an example using curl:

```bash
curl -X POST "http://localhost:8000/predict" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"inputs\":{\"sequence\":\"This is a test.\",\"candidate_labels\":[\"test\",\"exam\",\"check\"]}}"
```

The server will respond with the prediction results from the model server.

## Note

### How to make predictions

Use the `/predict` endpoint to make POST requests with the appropriate inputs for the chosen model. The input data formats for each model are as follows:

- **Zero-shot Classification**:

```json
{
  "inputs": {
    "sequence": "text_sequence",
    "candidate_labels": ["label1", "label2", ..., "labelN"]
  }
}
```

- **Object Detection**:

```json
{
  "inputs": "image.jpg"
}
```

- **Token Classification**:

```json
{
  "inputs": "text_input"
}
```

- **Text Generation**:

```json
{
  "inputs": "text_input"
}
```

You can make these requests using a tool like curl, Postman, or any HTTP client in a programming language of your choice.

The application currently uses predefined model servers. If you want to use your own model servers, you need to modify the `model_deployed_url` and `hf_pipeline` variables in `app.py`.

If you encounter any issues, please open an issue on this GitHub repository.

## Contributing

If you want to contribute to this project, please create a pull request. Any contributions, big or small, are welcomed and appreciated!

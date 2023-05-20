import subprocess
import sys

def install_library(library_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])

# Install required libraries
required_libraries = ["fastapi", "pydantic", "requests"]
for library in required_libraries:
    install_library(library)

# Continue with the rest of your code
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict, Union
import base64
from urllib.parse import urljoin

hp=("text-generation","zero-shot-classification","object-detection","token-class")
mdu=("https://text-generation-intern-mohsina.demo1.truefoundry.com/","https://zero-shot-classification-intern-mohsina.demo1.truefoundry.com/","https://object-detection-intern-mohsina.demo1.truefoundry.com/","https://token-class-intern-mohsina.demo1.truefoundry.com/")
app = FastAPI()
# hf_pipeline = hp[int(sys.argv[1])-1]
# model_deployed_url = mdu[int(sys.argv[1])-1]
hf_pipeline = "token-class"
model_deployed_url = "https://token-class-intern-mohsina.demo1.truefoundry.com/"

class Input(BaseModel):
    inputs: Any

def convert_to_v2_format(inputs: Any, pipeline: str) -> Dict:
    if pipeline == "zero-shot-classification":
        v2_format_data = {
            "inputs": [
                {
                    "name": "array_inputs",
                    "shape": [1, 1],
                    "datatype": "BYTES",
                    "data": [inputs['sequence']]
                },
                {
                    "name": "candidate_labels",
                    "shape": [1, len(inputs['candidate_labels'])],
                    "datatype": "BYTES",
                    "data": inputs['candidate_labels']
                }
            ]
        }

    elif pipeline == "object-detection":
        with open(inputs, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
        v2_format_data = {
            "inputs": [
                {
                    "name": "inputs",
                    "shape": [1, 1],
                    "datatype": "BYTES",
                    "data": [encoded_image],
                    "parameters": {"content_type": "base64"},
                }
            ]
        }

    elif pipeline == "text-generation":
        v2_format_data = {
            "inputs": [
                {
                    "name": "array_inputs",
                    "shape": [1, 1],
                    "datatype": "BYTES",
                    "data": [inputs]
                }
            ]
        }

    elif pipeline == "token-class":
        v2_format_data = {
            "inputs": [
                {
                    "name": "args",
                    "shape": [1, 1],
                    "datatype": "BYTES",
                    "data": [inputs]
                }
            ]
        }
    else:
        raise ValueError(f"Unsupported pipeline: {pipeline}")

    return v2_format_data

@app.post("/predict")
def predict(input: Input):
    print(hf_pipeline)
    v2_format_data = convert_to_v2_format(input.inputs, hf_pipeline)
    response = requests.post(urljoin(model_deployed_url, f'v2/models/{hf_pipeline}/infer'),json=v2_format_data)
    return response.json()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000)
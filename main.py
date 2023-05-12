import json
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from converters.json_to_xml import json_to_xml
from converters.xml_to_json import xml_to_json

app = FastAPI()

class ConverterRequest(BaseModel):
    text: str

class ConverterResponse(BaseModel):
    text: str

@app.post('/converters/libs/json_to_xml')
def main(request: ConverterRequest):
    data_json =  json.loads(request.text)
    converted = json_to_xml(data_json)
    return ConverterResponse(text=converted)

@app.post('/converters/libs/xml_to_json')
def main(request: ConverterRequest):
    try:
        data_xml = request.text
        converted = xml_to_json(data_xml)
        return ConverterResponse(text=converted)
    except Exception:
        print("")

@app.get("/")
def index():
    return "Welcome to converter"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
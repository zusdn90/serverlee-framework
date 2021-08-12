import os
from fastapi import FastAPI
from mangum import Mangum

stage = os.environ.get('STAGE', None)

# swagger url 설정
openapi_prefix = f"/{stage}" if stage else "/"
app = FastAPI(title= "My Serverless App", openapi_prefix=openapi_prefix)

@app.get("/hello")
def hello_world():
    return {
        "message" : "hello world"
    }

@app.get("/test")
def test():
    return {
        "message" : "test world"
    }

handler = Mangum(app)

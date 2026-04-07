#api
import fastapi


app = fastapi.FastAPI()

url = "http://127.0.0.1:8000"

@app.get("/status")
def ok_daccord():
    return {'status': 'ok'}

@app.post("/predict")
def prediction():
    pass
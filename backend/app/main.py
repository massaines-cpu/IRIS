#api
import fastapi
from pydantic import BaseModel

app = fastapi.FastAPI()

url = "http://127.0.0.1:8000"

class Donnees(BaseModel):
    longueur_petale : int
    largeur_petale : int
    longueur_sepale : int
    largeur_sepale : int

@app.get("/status")
def ok_daccord():
    return {'status': 'ok'}

@app.post("/predict")
def prediction():
    pass
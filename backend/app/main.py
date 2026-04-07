#api
import fastapi
import joblib
from pydantic import BaseModel

modele_path = ('./model/belles_fleurs.joblib')
modele = joblib.load(modele_path)

app = fastapi.FastAPI()

url = "http://127.0.0.1:8000"

class Donnees(BaseModel):
    longueur_sepale: float
    largeur_sepale: float
    longueur_petale : float
    largeur_petale : float

@app.get('/status')
def ok_daccord():
    return {'status': 'ok'}

@app.post("/predict")
def prediction(data: Donnees):
    fleur = [[
        data.longueur_sepale,
        data.largeur_sepale,
        data.longueur_petale,
        data.largeur_petale
    ]]
    print(fleur)
    prediction = modele.predict(fleur)
    return {'prediction': str(prediction[0])}

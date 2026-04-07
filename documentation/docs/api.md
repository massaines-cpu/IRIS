# API Iris Predictor

Cette API permet de prédire l’espèce d’une fleur Iris à partir de mesures de sépales et pétales.  
Elle est basée sur un modèle **RandomForestClassifier** entraîné sur le dataset Iris et déployée avec **FastAPI**.


## Endpoints

### GET `/status`

- **Description** : Vérifie que l’API est en ligne.  
- **Exemple de requête :**

```bash
curl -X GET http://localhost:8000/status
{
  "status": "ok"
}
```
### POST /predict
Description : Prédit l’espèce d’Iris selon les mesures fournies.
Payload JSON attendu :
```
{
  "longueur_sepale": 1.4,
  "largeur_sepale": 0.2,
  "longueur_petale": 5.1,
  "largeur_petale": 3.5
}
```
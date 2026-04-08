# Entraînement du modèle — Classification des Iris

## Description

Ca entraîne un modèle de classification **Random Forest** sur le dataset Iris. Il prédit l'espèce d'une fleur (`Species`) à partir de ses dimensions (sépales et pétales), puis sauvegarde le modèle entraîné au format `.joblib`.

## Données

| Fichier | Format | Source |
|--------|--------|--------|
| `Iris.csv` | CSV | Dataset Iris (150 exemples, 3 espèces) |

### Features utilisées

| Feature | Description |
|---------|-------------|
| `SepalLengthCm` | Longueur du sépale (cm) |
| `SepalWidthCm` | Largeur du sépale (cm) |
| `PetalLengthCm` | Longueur du pétale (cm) |
| `PetalWidthCm` | Largeur du pétale (cm) |

### Variable cible

- `Species` : espèce de la fleur (`Iris-setosa`, `Iris-versicolor`, `Iris-virginica`)

---

## Pipeline d'entraînement

### 1. Chargement des données
```python
data = pd.read_csv(data_path)
```

### 2. Séparation features / cible
```python
X = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = data['Species']
```

### 3. Split train / test
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)
```
- **Test size** : 33% des données
- **random_state** : 0 (reproductibilité)

### 4. Entraînement
```python
model = RandomForestClassifier(random_state=0)
model.fit(X_train, y_train)
```
- Algorithme : **Random Forest** (scikit-learn)
- Hyperparamètres : valeurs par défaut (100 arbres)

### 5. Évaluation
```python
accuracy_score(y_test, y_predict)
classification_report(y_test, y_predict)
```

### 6. Sauvegarde du modèle
```python
joblib.dump(model, '../model/belles_fleurs.joblib')
```
Le modèle est sauvegardé dans `../model/belles_fleurs.joblib` pour être utilisé par l'API.

---

## Dépendances

```
scikit-learn
pandas
joblib
```

---

## Utilisation

```bash
python train.py
```

> ⚠️ Modifier `data_path` si le fichier `Iris.csv` est dans un autre répertoire.

---

## Sorties

| Fichier | Description |
|--------|-------------|
| `../model/belles_fleurs.joblib` | Modèle entraîné, prêt à être chargé par l'API |
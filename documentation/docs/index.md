# Projet IRIS

## Objectif
Prédire l'espèce d'une fleur Iris à partir de ses caractéristiques.
Déployer sur github
Déployer sur Dockerhub
Déployer sur Azure

## Données
- SepalLengthCm : longueur des sépales
- SepalWidthCm : largeur des sépales
- PetalLengthCm : longueur des pétales
- PetalWidthCm : largeur des pétales

## Modèle
J'ai utilisé un RandomForestClassifier.

## Utilisation

```python
model.predict([[5.1, 3.5, 1.4, 0.2]])
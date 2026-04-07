#train

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import pandas as pd
import joblib
data_path = '/Users/nini/IRIS/mes_petites_fleurs/Iris.csv'
data = pd.read_csv(data_path)
print(data.head())

X = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
y = data['Species']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)
model = RandomForestClassifier(random_state=0)
model.fit(X_train, y_train)

y_predict = model.predict(X_test)

print('accuary', accuracy_score(y_test, y_predict))
print('classification report', classification_report(y_test, y_predict))

joblib.dump(model, 'belles_fleurs.joblib')
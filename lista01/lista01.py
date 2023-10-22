from sklearn.datasets import load_iris
from sklearn.datasets import load_wine

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

"""Base de dados importado pela SKlearn"""
iris = load_iris()
wine = load_wine()
X_iris, y_iris = iris.data, iris.target
X_wine, y_wine = wine.data, wine.target

"""Split da base 80-20"""
X_train_iris, X_test_iris, y_train_iris, y_test_iris = train_test_split(X_iris, y_iris, test_size=0.2, random_state=42)
X_train_wine, X_test_wine, y_train_wine, y_test_wine = train_test_split(X_wine, y_wine, test_size=0.2, random_state=42)

"""Inicia e treina a arvore"""
model_iris = DecisionTreeClassifier()
model_wine = DecisionTreeClassifier()
model_iris.fit(X_train_iris, y_train_iris)
model_wine.fit(X_train_wine, y_train_wine)

"""Predição da base de dados com o conjunto teste"""
y_pred_iris = model_iris.predict(X_test_iris)
y_pred_wine = model_wine.predict(X_test_wine)

"""Taxas de acerto: """
print(f"Taxa de Acerto para Iris: {accuracy_score(y_test_iris, y_pred_iris) * 100:.2f}% \n "
      f"Taxa de Acerto para Wine: {accuracy_score(y_test_wine, y_pred_wine) * 100:.2f}%")


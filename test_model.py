# test_model.py
import joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset and model
iris = load_iris()
X = iris.data
y = iris.target
model = joblib.load('iris_model.pkl')

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Make predictions and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
assert accuracy > 0.9, f"Model accuracy too low: {accuracy}"

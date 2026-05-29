from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

                       
iris = load_iris()
X = iris.data
y = iris.target

                                                  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

                                  
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

                                     
joblib.dump(model, 'random_forest_model.pkl')

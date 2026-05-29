from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

                       
data = load_iris()
features = data.data
labels = data.target

                                               
X_train_split, X_test_split, y_train_split, y_test_split = train_test_split(features, labels, test_size=0.25, random_state=21)

                                        
classifier = LogisticRegression(max_iter=250, random_state=21)
classifier.fit(X_train_split, y_train_split)

                                     
joblib.dump(classifier, 'lr_model.pkl')
